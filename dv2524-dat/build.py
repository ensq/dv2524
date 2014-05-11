#!/bin/python
# Build script compiling and copying results .dat-segments into build directory dv2524-bin/.

import os
import glob
import numpy
import shutil
import fileinput

g_iam = "dv2524-dat/build.py"

def avg(p_iam, p_filename):
    file = open(p_filename, 'r')

    mss = []
    for line in file:
        ms = float(line)
        mss.append(ms)
    msavg = numpy.average(mss)
    msstd = numpy.std(mss)
    msmin = numpy.min(mss)
    msmax = numpy.max(mss)
    print(p_iam + ": Parsed file " + p_filename + " has the following attributes: \n\tAvg: " + str(msavg) + "\n\tStd: " + str(msstd) + "\n\tMin: " + str(msmin) + "\n\tMax: " + str(msmax))

    file.close()
    return msavg

def correct_profiling(p_iam, p_filename, p_offset):
    mss = []

    avgBefore = avg(p_iam, p_filename)

    file = open(p_filename, "r+")
    for line in file:
        ms = float(line)
        mss.append(ms)
    file.truncate() # Clear file contents.
    file = open(p_filename, 'w')
    for ms in mss:
        ms = ms + p_offset
        file.write(str(ms) + '\n')
    file.close()

    avgAfter = avg(p_iam, p_filename)

    print(p_iam + ": Offset profiling measurements in " + p_filename + " with " + str(p_offset) + ", effectively reducing the average from " + str(avgBefore) + " to " + str(avgAfter) + ".")

def sort_file(p_iam, p_filename):
    mss = []

    file = open(p_filename, "r+")
    for line in file:
        ms = float(line)
        mss.append(ms)
    file.truncate() # Clear file contents.

    mss = sorted(mss)
    msMax = max(mss)
    msMin = min(mss)

    file = open(p_filename, 'w')
    for ms in mss:
        file.write(str(ms) + '\n')
    file.close()

    print(p_iam + ": Sorted file " + p_filename + " with minimum entry " + str(msMin) + " and maximum entry " + str(msMax) + ".")

# Entry point:
print(g_iam + ": Enter...")

buildDirectory = "../dv2524-bin/"
# We start off by copying all data sets (file extension .dat) into the build directory:
datasets = glob.iglob(os.path.join(".", "*.dat"))
for file in datasets:
    shutil.copy2(file, buildDirectory)
# We then change the current working directory to said build directory, to ensure the original source data sets are not modified.
os.chdir(buildDirectory)

# The profiling method used to measure elapsed time on the Simics platform, that is the platform used to collect results for the simics- and para- prefixes, is expected to carry with it some measurement overhead (see thesis.pdf). We compile the expected outcome of this overhead, and compile new results, from the raw results based off of this overhead.
profiling_overhead = avg(g_iam, "profile.dat")

# Sort profiling overhead analysis for the purposes of visualizing error deviations minimum and maximum:
sort_file(g_iam, "profile.dat")

files_need_correcting = glob.glob("simics*.dat")
files_need_correcting += glob.glob("para*.dat")
for filename in files_need_correcting:
    correct_profiling(g_iam, filename, -profiling_overhead)

# Before exiting, we change the current working directory back to the original one:
os.chdir("../dv2524-dat/")

print(g_iam + ": Exit.")
