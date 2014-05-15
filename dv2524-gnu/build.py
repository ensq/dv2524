#!/bin/python
# Builds graphs using GNUplot.

import os
import subprocess

g_iam = "dv2524-gnu/build.py"
g_gnuHistograms = "../dv2524-gnu/histograms.gnu"
g_gnuHistogramsStacked = "../dv2524-gnu/histogramsstacked.gnu"

# Entry point:
print(g_iam + ": Enter...")

# Start by changing directory, as we want to work with possibly modified plots in the build directory:
os.chdir("../dv2524-bin/")

# Draw 3x2 histograms:
cmd = "gnuplot -e \"arg_data1='%s';arg_data2='%s';arg_data3='%s';arg_data4='%s';arg_data5='%s';arg_data6='%s';arg_terminal='%s';arg_output='%s'\" " + g_gnuHistograms;
arg1 = "simicschess60x60.dat"
arg2 = "parachess60x60.dat"
arg3 = "simicschess84x84.dat"
arg4 = "parachess84x84.dat"
arg5 = "simicschess118x118.dat"
arg6 = "parachess118x118.dat"
arg7 = "epslatex"
arg8 = "../dv2524-bin/gnuhistogramssimicsparachess.tex"
sp = subprocess.Popen(cmd % (arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8), shell=True)
sp.wait()

arg1 = "simicsjulia225.dat"
arg2 = "parajulia225.dat"
arg3 = "simicsjulia450.dat"
arg4 = "parajulia450.dat"
arg5 = "simicsjulia900.dat"
arg6 = "parajulia900.dat"
arg7 = "epslatex"
arg8 = "../dv2524-bin/gnuhistogramssimicsparajulia.tex"
sp = subprocess.Popen(cmd % (arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8), shell=True)
sp.wait()

arg1 = "simicsphong1448x1448.dat"
arg2 = "paraphong1448x1448.dat"
arg3 = "simicsphong2048x2048.dat"
arg4 = "paraphong2048x2048.dat"
arg5 = "simicsphong2896x2896.dat"
arg6 = "paraphong2896x2896.dat"
arg7 = "epslatex"
arg8 = "../dv2524-bin/gnuhistogramssimicsparaphong.tex"
sp = subprocess.Popen(cmd % (arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8), shell=True)
sp.wait()

# Draw 3x1 histograms:
cmd = "gnuplot -e \"arg_data1='%s';arg_data2='%s';arg_data3='%s';arg_title1='%s';arg_title2='%s';arg_title3='%s';arg_terminal='%s';arg_output='%s'\" " + g_gnuHistogramsStacked;

arg1 = "hostchess84x84.dat"
arg2 = "hostjulia450.dat"
arg3 = "hostphong2048x2048.dat"
arg4 = "Chess"
arg5 = "Julia"
arg6 = "Phong"
arg7 = "epslatex"
arg8 = "gnuhistogramshost.tex"
sp = subprocess.Popen(cmd % (arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8), shell=True)
sp.wait()

arg1 = "qemuchess84x84.dat"
arg2 = "qemujulia450.dat"
arg3 = "qemuphong2048x2048.dat"
arg4 = "Chess"
arg5 = "Julia"
arg6 = "Phong"
arg7 = "epslatex"
arg8 = "gnuhistogramsqemu.tex"
sp = subprocess.Popen(cmd % (arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8), shell=True)
sp.wait()

# Change working directory back before exiting:
os.chdir("../dv2524-gnu/")

print(g_iam + ": Exit.")

# Old invocation of lone histograms:
#benchmarks = \
#	[["julia225.dat","julia450.dat","julia900.dat"],\
#	["phong1448x1448.dat", "phong2048x2048.dat", "phong2896x2896.dat"],\
#	["chess60x60.dat", "chess84x84.dat", "chess118x118.dat"]]
#platforms = ["simics", "para"]

#cmd = "gnuplot -e \"arg_data1='%s';arg_data2='%s';arg_data3='%s';arg_output='%s'\" demo.gpt";
#for platform in platforms:
#	for benchmark in benchmarks:
#		arg1 = "results/" + platform + benchmark[0]
#		arg2 = "results/" + platform + benchmark[1]
#		arg3 = "results/" + platform + benchmark[2]
#		arg4 = platform + benchmark[0] + ".svg"

#		sp = subprocess.Popen(cmd % (arg1, arg2, arg3, arg4), shell=True)
#		sp.wait()
