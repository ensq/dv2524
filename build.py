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
    subbuild(os.getcwd() + "/dv2524-con")
    subbuild(os.getcwd() + "/dv2524-bst")
    subbuild(os.getcwd() + "/dv2524-pac")
    subbuild(os.getcwd() + "/dv2524-git")
    subbuild(os.getcwd() + "/dv2524-sty") # Both proposal, thesis and opposition report use the same style.

def buildProposal(p_from):
    print(p_from + ": Building Proposal document...")
    buildCommon()

    subbuild(os.getcwd() + "/dv2524-res", "--target proposal")
    subbuild(os.getcwd() + "/dv2524-bib", "--target proposal")
    subbuild(os.getcwd() + "/dv2524-pro")
    shutil.copyfile("dv2524-bin/proposal.pdf", "proposal.pdf")

def buildThesis(p_from):
    print(p_from + ": Building Thesis document...")
    buildCommon()

    subbuild(os.getcwd() + "/dv2524-img")
    subbuild(os.getcwd() + "/dv2524-tab")
    subbuild(os.getcwd() + "/dv2524-fig")
    subbuild(os.getcwd() + "/dv2524-dat")
    subbuild(os.getcwd() + "/dv2524-gnu")
    subbuild(os.getcwd() + "/dv2524-res", "--target thesis")
    subbuild(os.getcwd() + "/dv2524-bib", "--target thesis")
    subbuild(os.getcwd() + "/dv2524-the")
    shutil.copyfile("dv2524-bin/thesis.pdf", "thesis.pdf")

def buildOpposition(p_from):
    print(p_from + ": Building Opposition Report document...")
    buildCommon()

    subbuild(os.getcwd() + "/dv2524-opp")
    shutil.copyfile("dv2524-bin/opposition.pdf", "opposition.pdf")

def buildPresentation(p_from):
    print(p_from + ": Building Presentation document...")
    buildCommon()

    subbuild(os.getcwd() + "/dv2524-img")
    subbuild(os.getcwd() + "/dv2524-fig")
    subbuild(os.getcwd() + "/dv2524-pre")
    shutil.copyfile("dv2524-bin/presentation.pdf", "presentation.pdf")

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

build_proposal = False
build_thesis = False
build_opposition = False
build_presentation = False
try:
  target
except NameError:
    build_proposal = True
    build_thesis = True
    build_opposition = True
    build_presentation = True
else:
    if target=="proposal":
        build_proposal = True
    elif target=="thesis":
        build_thesis = True
    elif target=="opposition":
        build_opposition = True
    elif target=="presentation":
        build_presentation = True
    else:
        print(g_iam + ": Invalid target!")
        usage(g_iam)
        sys.exit(2)

if build_proposal==True:
    deleteFile(g_iam, "proposal.pdf")
    buildProposal(g_iam)
if build_thesis==True:
    deleteFile(g_iam, "thesis.pdf")
    buildThesis(g_iam)
if build_opposition==True:
    deleteFile(g_iam, "opposition.pdf")
    buildOpposition(g_iam)
if build_presentation==True:
    deleteFile(g_iam, "presentation.pdf")
    buildPresentation(g_iam)

print(g_iam + ": Exit.")
