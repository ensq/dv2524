#!/bin/python
# Script copying the entire contents (except itself) to the dv2524-bin/ build directory.

import os
import shutil
import distutils.core

g_iam = "dv2524-con/build.py"

# Entry point:
print(g_iam + ": Enter...")

if not os.path.isfile("Intel-logo.pdf"):
    print(g_iam + ": Warning - No Intel Logo present. Using placeholder image.")
    shutil.copyfile("pdficon_large.pdf", "Intel-logo.pdf")

srcDir = os.listdir(".")
dstDir = "../dv2524-bin/"

for files in srcDir:
	if not files.endswith(".py"):
		shutil.copy(files, dstDir)

print(g_iam + ": Exit.")
