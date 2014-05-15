#!/bin/python
# Build script copying table .tex-files into build directory dv2524-bin/.

import os
import glob
import shutil

g_iam = "dv2524-tab/build.py"

# Entry point:
print(g_iam + ": Enter...")

buildDirectory = "../dv2524-bin/"
# We start off by copying all data sets (file extension .tex) into the build directory:
tables = glob.iglob(os.path.join(".", "*.tex"))
for table in tables:
    shutil.copy2(table, buildDirectory)

print(g_iam + ": Exit.")