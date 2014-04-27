#!/bin/python
# Script compressing document-specific resources (images etc.) to dv2524-bin/ directory.

import os
import sys
import getopt
import shutil
import zipfile
import distutils.core

g_iam = "dv2524-res/build.py"

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
    unzipToDir(g_iam, "dv2524-res-thesis.zip", ".")
    distutils.dir_util.copy_tree("./dv2524-res-thesis", "../dv2524-bin")
    clean(g_iam, "dv2524-res-thesis")
elif target=="proposal":
    unzipToDir(g_iam, "dv2524-res-proposal.zip", ".")
    distutils.dir_util.copy_tree("./dv2524-res-proposal", "../dv2524-bin")
    clean(g_iam, "dv2524-res-proposal")
else:
    usage(g_iam)
    sys.exit(2)

print(g_iam + ": Exit.")
