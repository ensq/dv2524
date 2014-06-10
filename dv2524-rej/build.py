#!/bin/python
# Script building thesis rejoinder.

import os
import glob
import shutil
import subprocess

g_iam = "dv2524-rej/build.py"

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
print("Calling git checkout; invoking post-checkout git hook...")
subprocess.call(["git", "checkout"])

print("Building LaTeX-document with pdflatex...")
subprocess.call("pdflatex rejoinder", shell=True)
subprocess.call("pdflatex rejoinder", shell=True)
subprocess.call("pdflatex rejoinder", shell=True)

# When build has completed, reset working directory back to original directory:
os.chdir("../dv2524-rej/")

print(g_iam + ": Exit.")
