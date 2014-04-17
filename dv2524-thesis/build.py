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

def Clean():
  print("Cleaning...")
  for file in os.listdir('.'):
    if file.endswith(".aux") \
    or file.endswith(".bbl") \
    or file.endswith(".blg") \
    or file.endswith(".log") \
    or file.endswith(".out") \
    or file.endswith(".bib"):
      os.remove(file)

print("dv2524-thesis/build.py")
print("---\n")

# Clean:
Clean()

# Unzip packages
print("Uncompressing...")
with zipfile.ZipFile("../dv2524-packages/gitinfo.zip", 'r') as zip:
  zip.extractall("../dv2524-packages")
with zipfile.ZipFile("../dv2524-encl/dv2524-encl.zip", 'r') as zip:
  zip.extractall("../dv2524-encl")

# Create original bib-files containing desired entries:
# Said entries are copied into files with an additional '.bib' appended to the filename (in case the user is building on my Windows-machine using MiKTeX).
bibfiles = ["../dv2524-bib/papers.bib", \
  "../dv2524-bib/magazines.bib", \
  "../dv2524-bib/dissertations.bib", \
  "../dv2524-bib/inproceedings.bib", \
  "../dv2524-bib/journals.bib", \
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

# Copy files into build directory:
print("Copying files into build directory...")
shutil.copyfile("../dv2524-packages/gitinfo/gitinfo.sty", "gitinfo.sty")
shutil.copyfile("../dv2524-packages/gitinfo/gitsetinfo.sty", "gitsetinfo.sty")
# Use distutils.dir_util.copy_tree() to copy entire directories recursively later on.

print("Building LaTeX-document with pdflatex...")
# Build intermediate .aux-files and symbol tree:
subprocess.call(["pdflatex", "thesis"])

# Build [multibib] bibliography:
subprocess.call(["bibtex", "bib.aux"])
subprocess.call(["bibtex", "ref.aux"])

subprocess.call(["pdflatex", "thesis"])
subprocess.call(["pdflatex", "thesis"])

# Clean again:
Clean()

# evince thesis.pdf
