#!/bin/python
# Script unpacking .sty (and .cls, etc.) for relevant document and copying said files into the dv2524-bin/ directory.

import os
import sys
import getopt
import shutil
import zipfile
import distutils.core

g_iam = "dv2524-sty/build.py"

def usage(p_from):
  print(p_from + ": Usage: " + sys.argv[0] + " -t TARGET")

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

try:
    opts, args = getopt.getopt( sys.argv[1:], "t:h", ["target=", "help="] )
except getopt.GetoptError as e:
    print( e )
    sys.exit( 2 )

for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage(g_iam)
        sys.exit(2)
    elif opt in ('-t', '--target'):
        target = arg
    else:
        usage(g_iam)
        sys.exit(2)
if len(opts)<1:
    usage(g_iam)
    sys.exit(2)

if target=="thesis":
    unzipToDir(g_iam, "dv2524-sty-thesis.zip", ".")
    distutils.dir_util.copy_tree("./dv2524-sty-thesis", "../dv2524-bin")
    clean(g_iam, "dv2524-sty-thesis")
elif target=="proposal":
    print(g_iam + ": Not yet implemented!")
    usage(g_iam)
    sys.exit(2)
else:
    usage(g_iam)
    sys.exit(2)

print(g_iam + ": Exit.")
