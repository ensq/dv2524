#!/bin/python
# Builds graphs using GNUplot.

import subprocess

g_iam = "dv2524-gpt/build.py"

# Entry point:
print(g_iam + ": Enter...")

# TODO: Delete old plots.

benchmarks = \
	[["julia225.ms","julia450.ms","julia900.ms"],\
	["phong1448x1448.ms", "phong2048x2048.ms", "phong2896x2896.ms"],\
	["chess60x60.ms", "chess84x84.ms", "chess118x118.ms"]]
platforms = ["simics", "para"]

cmd = "gnuplot -e \"arg_data1='%s';arg_data2='%s';arg_data3='%s';arg_output='%s'\" demo.gpt";
for platform in platforms:
	for benchmark in benchmarks:
		arg1 = "results/" + platform + benchmark[0]
		arg2 = "results/" + platform + benchmark[1]
		arg3 = "results/" + platform + benchmark[2]
		arg4 = platform + benchmark[0] + ".png"

		sp = subprocess.Popen(cmd % (arg1, arg2, arg3, arg4), shell=True)
		sp.wait()

print(g_iam + ": Exit.")