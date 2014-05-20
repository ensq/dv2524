#!/bin/python
# Script unpacking .sty (and .cls, etc.) for relevant document and copying said files into the dv2524-bin/ directory.

import os
import sys
import shutil
import zipfile
import distutils.core

g_iam = "dv2524-sty/build.py"

def unzipToDir(p_from, p_source, p_target):
    print(p_from + ": Unzipping " + p_source + " to " + p_target + " ...")
    with zipfile.ZipFile(p_source, 'r') as zip:
      zip.extractall(p_target)

def clean(p_from, p_dir):
    print(p_from + ": Deleting " + p_dir +"/ directory...")
    try:
        shutil.rmtree("./" + p_dir)
    except Exception: # I.e. not found.
        pass

# Entry point:
print(g_iam + ": Enter...")

unzipToDir(g_iam, "bth-thesis-latex.zip", ".")
distutils.dir_util.copy_tree("./bth-thesis-latex", "../dv2524-bin")
clean(g_iam, "bth-thesis-latex")
    
print(g_iam + ": Exit.")
