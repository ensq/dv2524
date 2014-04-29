#!/bin/python
# Script copying hooks into .git/hook/ directory.

import os
import shutil
import zipfile
import distutils.core

g_iam = "dv2524-git/build.py"

def unzipToDir(p_from, p_source, p_target):
    print(p_from + ": Unzipping " + p_source + " to " + p_target + " ...")
    with zipfile.ZipFile(p_source, 'r') as zip:
      zip.extractall(p_target)

def clean(p_from):
    print(p_from + ": Deleting hooks/ directory...")
    try:
        shutil.rmtree("./hooks")
    except Exception: # I.e. not found.
        pass

# Entry point:
print(g_iam + ": Enter...")
unzipToDir(g_iam, "hooks.zip", "./")
distutils.dir_util.copy_tree("./hooks", "../.git/hooks")

# Set file permissions to allow execution:
os.chmod("../.git/hooks/post-checkout", 0777) # WARNING: Would need changing if upgrade to python 3.
os.chmod("../.git/hooks/post-commit", 0777) # WARNING: Would need changing if upgrade to python 3.
os.chmod("../.git/hooks/post-merge", 0777) # WARNING: Would need changing if upgrade to python 3.

clean(g_iam)
print(g_iam + ": Exit.")
