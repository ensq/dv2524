#!/bin/python
# Script unpacking contents of dv2524-packages/ into dv2524-bin/ directory.

import os
import shutil
import zipfile
import distutils.core

g_iam = "dv2524-pac/build.py"

def unzipToDir(p_from, p_source, p_target):
    print(p_from + ": Unzipping " + p_source + " to " + p_target + " ...")
    with zipfile.ZipFile(p_source, 'r') as zip:
      zip.extractall(p_target)

def clean(p_from):
    print(p_from + ": Deleting gitinfo/ directory...")
    try:
        shutil.rmtree("./gitinfo")
    except Exception: # I.e. not found.
        pass

# Entry point:
print(g_iam + ": Starting...")

# Unpack and copy gitinfo package contents to dv2524-bin/ directory:
unzipToDir(g_iam, "gitinfo.zip", ".")
distutils.dir_util.copy_tree("./gitinfo", "../dv2524-bin")

clean(g_iam)
print(g_iam + ": Done.")

#def unzipToDirPlain(p_from, p_source, p_target):
#    print(p_from + ": Unzipping " + p_source + " to " + p_target + " whilst ignoring tree structure...")
#    with zipfile.ZipFile(p_source) as zip:
#        for entry in zip.namelist():
#            filename = os.path.basename(entry)
#            if filename: # If not directory.
#                source = zip.open(entry)
#                target = file(os.path.join(p_target), "wb")
#                with source, target:
#                    shutil.copyfileobj(source, target)
