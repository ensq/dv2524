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

def Clean(p_except):
  cleanendings = [".aux", ".bbl", ".blg", ".log", ".out", ".bib", ".bst", ".sty", ".cls", ".toc", ".pdf", ".gin", ".glo"]
  print("Cleaning " + str(cleanendings) + " from build directory...")
  for file in os.listdir('.'):
      for cleanending in cleanendings:
          if file!=p_except and file.endswith(cleanending):
              os.remove(file)

def unzipToDir(p_filename, p_dirname):
    print("Unzipping " + p_filename + " to " + p_dirname + "...")
    with zipfile.ZipFile(p_filename, 'r') as zip:
      zip.extractall(p_dirname)

print("dv2524-thesis/build.py")
print("---\n")

# Clean build directory:
Clean(None)

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
bibfiles = ["../dv2524-bib/papers.bib",  \
  "../dv2524-bib/magazines.bib",         \
  "../dv2524-bib/dissertations.bib",     \
  "../dv2524-bib/inproceedings.bib",     \
  "../dv2524-bib/journals.bib",          \
  "../dv2524-bib/publications.bib"]
with open("thesisbibliography.bib", 'w') as ofile:
    for filename in bibfiles:
        with open(filename, 'r') as ifile:
            ofile.write(ifile.read())
shutil.copyfile("thesisbibliography.bib", "thesisbibliography.bib.bib")

reffiles = ["../dv2524-bib/technicaldocs.bib", \
  "../dv2524-bib/web.bib"]
with open("thesiswebreferences.bib", 'w') as ofile:
  for filename in reffiles:
    with open(filename, 'r') as ifile:
      ofile.write(ifile.read())
shutil.copyfile("thesiswebreferences.bib", "thesiswebreferences.bib.bib")

# Update git head, invoking [gitinfo] post-checkout hook:
subprocess.call(["git", "checkout"])

print("Building LaTeX-document with pdflatex...")
# Build intermediate .aux-files and symbol tree:
subprocess.call(["pdflatex", "thesis"])

# Build [glossaries] nomenclature:
subprocess.call(["makeglossaries", "thesis"])

# Build [multibib] bibliography:
subprocess.call(["bibtex", "bib.aux"])
subprocess.call(["bibtex", "ref.aux"])

subprocess.call(["pdflatex", "thesis"])
subprocess.call(["pdflatex", "thesis"])

# Clean again:
Clean("thesis.pdf")

# evince thesis.pdf
