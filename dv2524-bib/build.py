#!/bin/python
# Script concatenating .bib bibliographies and placing them into the dv2524-bib/ build directory.

import sys
import getopt
import shutil

g_iam = "dv2524-bib/build.py"

g_bibfiles = [\
    "../dv2524-bib/papers.bib",\
    "../dv2524-bib/magazines.bib",\
    "../dv2524-bib/dissertations.bib",\
    "../dv2524-bib/inproceedings.bib",\
    "../dv2524-bib/journals.bib",\
    "../dv2524-bib/publications.bib"]
g_reffiles = [\
    "../dv2524-bib/technicaldocs.bib",\
    "../dv2524-bib/web.bib"]
g_furfiles = [\
    "../dv2524-bib/dissertations.bib",\
    "../dv2524-bib/technicaldocs.bib"]

def usage(p_from):
  print(p_from + ": Usage: " + sys.argv[0] + " --target [thesis, proposal]")

def concatenate(p_from, p_ifilenames, p_ofilename):
    print(p_from + ": Concatenating files " + str(p_ifilenames) + " into " + p_ofilename + "...")
    with open(p_ofilename, 'w') as ofile:
        for filename in p_ifilenames:
            with open(filename, 'r') as ifile:
                ofile.write(ifile.read())

def copy(p_from, p_source, p_target):
    print(p_from + ": Copying " + p_source + " to " + p_target + "...")
    shutil.copyfile(p_source, p_target)

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
        bibprefix = arg
    else:
        usage(g_iam)
        sys.exit(2)
if len(opts)<1:
    usage(g_iam)
    sys.exit(2)

# Bibliography:
bibname = "../dv2524-bin/" + bibprefix + "bibliography.bib"
concatenate(g_iam, g_bibfiles, bibname)
copy(g_iam, bibname, bibname + ".bib")

# Web References:
bibname = "../dv2524-bin/" + bibprefix + "webreferences.bib"
concatenate(g_iam, g_reffiles, bibname)
copy(g_iam, bibname, bibname + ".bib")

# Further Reading:
bibname = "../dv2524-bin/" + bibprefix + "furtherreading.bib"
concatenate(g_iam, g_furfiles, bibname)
copy(g_iam, bibname, bibname + ".bib")

print(g_iam + ": Exit.")
