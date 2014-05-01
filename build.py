#!/bin/python
# Main build script. Takes lone argument indicating which document to build.
# Invoke accordingly: python build.py -t thesis

import os
import sys
import shutil
import getopt
import subprocess

g_iam = "build.py"

def deleteFile(p_from, p_filename):
    print(p_from + ": Removing " + p_filename + "...")
    try:
        os.remove(p_filename)
    except OSError:
        pass

def usage(p_from):
  print(p_from + ": Usage: " + sys.argv[0] + " -t [--target] TARGET")

def subbuild(p_dir, p_args = ""):
    bp = subprocess.Popen("python " + p_dir + "/build.py " + p_args, cwd=p_dir + "/", shell=True)
    bp.wait() # We want a synchronous build.

def buildCommon():
    subbuild(os.getcwd() + "/dv2524-bin")
    subbuild(os.getcwd() + "/dv2524-bst")
    subbuild(os.getcwd() + "/dv2524-pac")
    subbuild(os.getcwd() + "/dv2524-git")

def buildProposal(p_from):
    print(p_from + ": Building Proposal document...")
    buildCommon()

    subbuild(os.getcwd() + "/dv2524-sty", "--target proposal")
    subbuild(os.getcwd() + "/dv2524-res", "--target proposal")
    subbuild(os.getcwd() + "/dv2524-bib", "--target proposal")
    subbuild(os.getcwd() + "/dv2524-pro")
    shutil.copyfile("dv2524-bin/proposal.pdf", "proposal.pdf")

def buildThesis(p_from):
    print(p_from + ": Building Thesis document...")
    buildCommon()

    subbuild(os.getcwd() + "/dv2524-sty", "--target thesis")
    subbuild(os.getcwd() + "/dv2524-res", "--target thesis")
    subbuild(os.getcwd() + "/dv2524-bib", "--target thesis")
    subbuild(os.getcwd() + "/dv2524-the")
    shutil.copyfile("dv2524-bin/thesis.pdf", "thesis.pdf")

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

buildproposal = False
buildthesis = False
try:
  target
except NameError:
    buildproposal = True
    buildthesis = True
else:
    if target=="proposal":
        buildproposal = True
    elif target=="thesis":
        buildthesis = True
    else:
        print(g_iam + ": Invalid target!")
        usage(g_iam)
        sys.exit(2)

if buildproposal==True:
    deleteFile(g_iam, "proposal.pdf")
    buildProposal(g_iam)
if buildthesis==True:
    deleteFile(g_iam, "thesis.pdf")
    buildThesis(g_iam)

print(g_iam + ": Exit.")
