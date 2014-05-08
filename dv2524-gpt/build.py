#!/bin/python
# Builds graphs using GNUplot.

import subprocess

g_iam = "dv2524-gpt/build.py"

# Entry point:
print(g_iam + ": Enter...")

cmd = "gnuplot -e \"arg_data1='%s';arg_data2='%s';arg_data3='%s'\" demo.gpt";

arg1 = "results/paraphong1448x1448.ms"
arg2 = "results/paraphong2048x2048.ms"
arg3 = "results/paraphong2896x2896.ms"
for i in range(0,10):
	sp = subprocess.Popen(cmd % (arg1, arg2, arg3), shell=True)
	sp.wait()

print(g_iam + ": Exit.")