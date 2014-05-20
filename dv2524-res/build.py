#!/bin/python
# Script compressing document-specific resources (images etc.) to dv2524-bin/ directory.

import os
import sys
import getopt
import shutil
import distutils.core

g_iam = "dv2524-res/build.py"

def usage(p_from):
  print(p_from + ": Usage: " + sys.argv[0] + " -t TARGET")

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

buildDirectory = "../dv2524-bin/"
if target=="thesis":
    shutil.copy2("thesisindexstyle.ist", buildDirectory)
elif target=="proposal":
    shutil.copy2("androidopenglesdesignoverview.pdf", buildDirectory)
else:
    usage(g_iam)
    sys.exit(2)

print(g_iam + ": Exit.")
