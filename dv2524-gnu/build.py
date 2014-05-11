#!/bin/python
# Builds graphs using GNUplot.

import subprocess

g_iam = "dv2524-gnu/build.py"

# Entry point:
print(g_iam + ": Enter...")

# TODO: Delete old plots.

cmd = "gnuplot -e \"arg_data1='%s';arg_data2='%s';arg_data3='%s';arg_data4='%s';arg_data5='%s';arg_data6='%s';arg_terminal='%s';arg_output='%s'\" histograms.gnu";

arg1 = "results/simicsjulia225.ms"
arg2 = "results/parajulia225.ms"
arg3 = "results/simicsjulia450.ms"
arg4 = "results/parajulia450.ms"
arg5 = "results/simicsjulia900.ms"
arg6 = "results/parajulia900.ms"
arg7 = "epslatex"
arg8 = "../dv2524-bin/histograms.tex"

sp = subprocess.Popen(cmd % (arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8), shell=True)
sp.wait()

print(g_iam + ": Exit.")

# Old invocation of lone histograms:
#benchmarks = \
#	[["julia225.ms","julia450.ms","julia900.ms"],\
#	["phong1448x1448.ms", "phong2048x2048.ms", "phong2896x2896.ms"],\
#	["chess60x60.ms", "chess84x84.ms", "chess118x118.ms"]]
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
