#!/bin/python
# Main build script. Takes lone argument indicating which document to build.
# Invoke accordingly: python build.py -t thesis

import os
import sys
import shutil
import getopt
import subprocess

g_iam = "build.py"

def usage(p_from):
  print(p_from + ": Usage: " + sys.argv[0] + " -t [--target] TARGET")

def subbuild(p_dir, p_args = ""):
    bp = subprocess.Popen("python " + p_dir + "/build.py " + p_args, cwd=p_dir + "/", shell=True)
    bp.wait() # We want a synchronous build.

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

subbuild(os.getcwd() + "/dv2524-bin")
subbuild(os.getcwd() + "/dv2524-bst")
subbuild(os.getcwd() + "/dv2524-pac")
subbuild(os.getcwd() + "/dv2524-git")

if target=="thesis":
    subbuild(os.getcwd() + "/dv2524-sty", "--target thesis")
    subbuild(os.getcwd() + "/dv2524-res", "--target thesis")
    subbuild(os.getcwd() + "/dv2524-bib", "--prefix thesis")
    subbuild(os.getcwd() + "/dv2524-the")
    shutil.copyfile("dv2524-bin/thesis.pdf", "thesis.pdf")
#elif target=="proposal":
    # Build proposal.
#else:
#    print(g_iam + ": Invalid build target!")
#    usage(g_iam)
#    sys.exit(2).

print(g_iam + ": Exit.")
