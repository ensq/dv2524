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

# Entry point:
print(g_iam + ": Enter...")
unzipToDir(g_iam, "hooks.zip", "../.git/hooks")
print(g_iam + ": Exit.")
