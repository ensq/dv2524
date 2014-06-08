# scatters.gnu
# Renders three side-by-side scatterplots meant to visualize variance distribution.
# Requires GNUplot 4.6 or later.
# ---
# Invoke accordingly:
# gnuplot -e "arg_data1='../dv2524-bin/simicsphong1448x1448.dat';arg_data2='../dv2524-bin/simicsphong2048x2048.dat';arg_data3='../dv2524-bin/simicsphong2896x2896.dat';arg_data4='../dv2524-bin/simicsphong1448x1448no2.dat';arg_data5='../dv2524-bin/simicsphong2048x2048.dat';arg_data6='../dv2524-bin/simicsphong2896x2896no2.dat';arg_data7='../dv2524-bin/simicsphong1448x1448no3.dat';arg_data8='../dv2524-bin/simicsphong2048x2048no3.dat';arg_data9='../dv2524-bin/simicsphong2896x2896no3.dat';arg_output='out.png'" scatters.gnu
# ---

min(p_x, p_y) = (p_x<p_y) ? p_x : p_y
max(p_x, p_y) = (p_x>p_y) ? p_x : p_y
usage(p_iam) = sprintf("%s: Usage: gnuplot -e \"arg_data1='../dv2524-bin/simicsphong1448x1448.dat';arg_data2='../dv2524-bin/simicsphong2048x2048.dat';arg_data3='../dv2524-bin/simicsphong2896x2896.dat';arg_data4='../dv2524-bin/simicsphong1448x1448no2.dat';arg_data5='../dv2524-bin/simicsphong2048x2048.dat';arg_data6='../dv2524-bin/simicsphong2896x2896no2.dat';arg_data7='../dv2524-bin/simicsphong1448x1448no3.dat';arg_data8='../dv2524-bin/simicsphong2048x2048no3.dat';arg_data9='../dv2524-bin/simicsphong2896x2896no3.dat';arg_output='out.png'\" scatters.gnu", p_iam)
press(p_iam) = sprintf("%s: Press any key to continue.", p_iam)

# Entry point:
reset
iam = "dv2524-gnu/scatters.gnu"
print sprintf("%s: Enter...", iam)

if(!exists("arg_output")) { # Optional arguments.
    arg_output = "default.svg"
}
if(!exists("arg_data1")||!exists("arg_data2")||!exists("arg_data3")||!exists("arg_data4")||!exists("arg_data5")||!exists("arg_data6")||!exists("arg_data7")||!exists("arg_data8")||!exists("arg_data9")) { # Mandatory arguments.
    print usage(iam)
    pause -1 press(iam) # We should abort script here rather than simply pause it.
}

set terminal epslatex size 15cm, 22cm
set output arg_output

#set multiplot layout 1,3

set lmargin 2
set rmargin 2
set noborder
set ytics scale 0
unset xtics
unset key

do for[i=2:2] {
	files = ""
	if(i==1) {
		files=sprintf("%s %s %s", arg_data1, arg_data2, arg_data3)
	}
	if(i==2) {
		files=sprintf("%s %s %s", arg_data4, arg_data5, arg_data6)
	}
	if(i==3) {
		files=sprintf("%s %s %s", arg_data7, arg_data8, arg_data9)
	}

	plots_min = 9999.0
	plots_max = 0.0
	do for[i=1:3] {
		arg_data = word(files, i)
    	stats arg_data name "data" nooutput

    	std = data_stddev_y
		mean = data_mean_y
    	min = mean - std
    	max = mean + std

    	if(min<data_min_y) {
    		min = data_min_y
    	}
   		if(max>data_max_y) {
   			max = data_max_y
   		}

    	plots_min = min(plots_min, min)
    	plots_max = max(plots_max, max)
	}
	set yrange[plots_min:plots_max]

	data1 = word(files, 1)
	data2 = word(files, 2)
	data3 = word(files, 3)

	plot data1 pt 1 lt rgb "black",\
    	data2 pt 4 lt rgb "black",\
    	data3 pt 8 lt rgb "black"
}

#unset multiplot
set output # Terminate output file.

print sprintf("%s: Exit.", iam)
