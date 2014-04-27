#!/bin/python
# Script copying .bst resources to dv2524-bin/ directory.

import os
import shutil
import zipfile
import distutils.core

g_iam = "dv2524-bst/build.py"

def unzipToDir(p_from, p_source, p_target):
    print(p_from + ": Unzipping " + p_source + " to " + p_target + " ...")
    with zipfile.ZipFile(p_source, 'r') as zip:
      zip.extractall(p_target)

def clean(p_from):
    print(p_from + ": Deleting IEEEtranBST2/ directory...")
    try:
        shutil.rmtree("./IEEEtranBST2")
    except Exception: # I.e. not found.
        pass

# Entry point:
print(g_iam + ": Enter...")

unzipToDir(g_iam, "IEEEtranBST2.zip", ".")
distutils.dir_util.copy_tree("./IEEEtranBST2", "../dv2524-bin")

clean(g_iam)
print(g_iam + ": Exit.")
