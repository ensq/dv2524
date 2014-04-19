#!/bin/python
# Script building thesis document.
# ---
# Note that build.py treats some files as temporary ones (deleted prior to- and after each build) that may not be considered such by the user.
# Such a file is .bib, which is compiled by the script from an assortment of .bib-files in the dv2524-bib/ directory.
# ---

import os
import shutil
import zipfile
import subprocess

# Settings:
g_bibfiles = [\
    "../dv2524-bib/papers.bib",\
    "../dv2524-bib/magazines.bib",\
    "../dv2524-bib/dissertations.bib",\
    "../dv2524-bib/inproceedings.bib",\
    "../dv2524-bib/journals.bib",\
    "../dv2524-bib/publications.bib"]

g_reffiles = [\
    "../dv2524-bib/technicaldocs.bib",\
    "../dv2524-bib/web.bib"]

g_cleanfiletypes = [".aux", ".bbl", ".blg", ".log", ".out", ".bib", ".bst", ".sty", ".cls", ".toc", ".pdf", ".gin", ".glo"]

# Methods:
def clean():
    for ftype in g_cleanfiletypes:
        filesoftype = [f for f in os.listdir(".") if f.endswith(ftype)]
        print("Deleting " + str(len(filesoftype)) + " instances of filetype " + ftype + " from build directory...")
        for f in filesoftype:
            if f!="thesis.pdf": # Wouldn't wanna get rid of this.
                os.remove(f)

def unzipToDir(p_filename, p_dirname):
    print("Unzipping " + p_filename + " to " + p_dirname + "...")
    with zipfile.ZipFile(p_filename, 'r') as zip:
      zip.extractall(p_dirname)

def concatenate(p_ifilenames, p_ofilename):
    print("Concatenating files " + str(p_ifilenames) + " into " + p_ofilename + "...")
    with open(p_ofilename, 'w') as ofile:
        for filename in p_ifilenames:
            with open(filename, 'r') as ifile:
                ofile.write(ifile.read())

# Entry point:
print("dv2524-thesis/build.py")
print("---\n")

# Clean build directory:
clean()

# Uncompress resources used throughout build:
unzipToDir("../dv2524-packages/gitinfo.zip", "../dv2524-packages")
unzipToDir("../dv2524-encl/dv2524-encl.zip", "../dv2524-encl")
unzipToDir("../dv2524-bst/IEEEtranBST2.zip", "../dv2524-bst/IEEEtranBST2")
unzipToDir("../dv2524-sty/dv2524-sty-thesis.zip", "../dv2524-sty")
unzipToDir("../dv2524-git/hooks.zip", "../.git/hooks")

# Copy files into build directory:
print("Copying files into build directory...")
shutil.copyfile("../dv2524-packages/gitinfo/gitinfo.sty", "gitinfo.sty")
shutil.copyfile("../dv2524-packages/gitinfo/gitsetinfo.sty", "gitsetinfo.sty")
shutil.copyfile("../dv2524-bst/IEEEtranBST2/IEEEtranS.bst", "IEEEtranS.bst")
shutil.copyfile("../dv2524-sty/dv2524-sty-thesis/bth.cls", "bth.cls")
shutil.copyfile("../dv2524-sty/dv2524-sty-thesis/changepage.sty", "changepage.sty")
shutil.copyfile("../dv2524-sty/dv2524-sty-thesis/bth.pdf", "bth.pdf")
shutil.copyfile("../dv2524-sty/dv2524-sty-thesis/bthnotext.pdf", "bthnotext.pdf")
shutil.copyfile("../dv2524-encl/Intel-logo.pdf", "Intel-logo.pdf")
# Use distutils.dir_util.copy_tree() to copy entire directories recursively later on.

# Create original bib-files containing desired entries:
# Said entries are copied into files with an additional '.bib' appended to the filename (in case the user is building on my Windows-machine using MiKTeX).
concatenate(g_bibfiles, "thesisbibliography.bib")
shutil.copyfile("thesisbibliography.bib", "thesisbibliography.bib.bib")

concatenate(g_reffiles, "thesiswebreferences.bib")
shutil.copyfile("thesiswebreferences.bib", "thesiswebreferences.bib.bib")

# Update git head, invoking [gitinfo] post-checkout hook:
print("Calling git checkout; invoking post-checkout git hook...")
subprocess.call(["git", "checkout"])

print("Building LaTeX-document with pdflatex...")
# Build intermediate .aux-files and symbol tree:
subprocess.call(["pdflatex", "thesis"])

# Build [multibib] bibliography:
subprocess.call(["bibtex", "bib.aux"])
subprocess.call(["bibtex", "ref.aux"])

# Construct final thesis document - twice:
subprocess.call(["pdflatex", "thesis"])
subprocess.call(["pdflatex", "thesis"])

# Clean again:
clean()

print("Done.")
