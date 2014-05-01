#!/bin/python
# Script building proposal document.

import os
import glob
import shutil
import subprocess

g_iam = "dv2524-pro/build.py"

# Entry point:
print(g_iam + ": Enter...")

# Copy all files into build directory:
srcfiles = glob.iglob(os.path.join("./", "*.tex"))
for srcfile in srcfiles:
    if os.path.isfile(srcfile):
        shutil.copy2(srcfile, "../dv2524-bin/")

# After source files have been copied to build directory, change working directory to build directory:
os.chdir("../dv2524-bin/")

# Update git head, invoking [gitinfo] post-checkout hook:
print(g_iam + ": Calling git checkout; invoking post-checkout git hook...")
subprocess.call(["git", "checkout"])

print(g_iam + ": Building LaTeX-document with pdflatex...")
# Build intermediate .aux-files and symbol tree:
subprocess.call(["pdflatex", "proposal"])

# Build [multibib] bibliography:
print(g_iam + ": Building [multibib] bibliography...")
subprocess.call(["bibtex", "bib.aux"])
subprocess.call(["bibtex", "ref.aux"])

# Construct final thesis document - twice:
subprocess.call(["pdflatex", "proposal"])
subprocess.call(["pdflatex", "proposal"])

# When build has completed, reset working directory back to original directory:
os.chdir("../dv2524-pro/")

print(g_iam + ": Exit.")
