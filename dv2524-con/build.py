#!/bin/python
# Script copying the entire contents (except itself) to the dv2524-bin/ build directory.

import os
import shutil
import distutils.core

g_iam = "dv2524-con/build.py"

# Entry point:
print(g_iam + ": Enter...")

srcDir = os.listdir(".")
dstDir = "../dv2524-bin/"
for files in srcDir:
	if not files.endswith(".py"):
		shutil.copy(files, dstDir)

print(g_iam + ": Exit.")
