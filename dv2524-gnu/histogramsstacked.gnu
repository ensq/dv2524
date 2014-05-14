# histogramsstacked.gnu
# GNUplot script creating a 1x3 figure of histograms.
# Requires GNUplot 4.6 or later.
# ---
# Arguments:
# 1. Data set #1 : arg_data1
# 2. Data set #2 : arg_data2
# 3. Data set #3 : arg_data3
# 4. Title set #1 : arg_title1
# 5. Title set #2 : arg_title2
# 6. Title set #3 : arg_title3
# 7. Out Terminal : arg_terminal
# 8. Out Filename : arg_output
# ---

min(p_x, p_y) = (p_x<p_y) ? p_x : p_y
max(p_x, p_y) = (p_x>p_y) ? p_x : p_y
mapToBin(p_x, p_binWidth, p_binMin) = p_binWidth * (floor((p_x - p_binMin) / p_binWidth) + 0.5) + p_binMin # http://stackoverflow.com/a/19596160
usage(p_iam) = sprintf("%s: Usage: gnuplot -e \"arg_data1-3='data.dat';arg_title1-3='Title';arg_terminal='type';arg_output='filename.type'\" histogramsstacked.gnu", p_iam)
press(p_iam) = sprintf("%s: Press any key to continue.", p_iam)
default(p_iam, p_var) = sprintf("%s: Warning, using default var: %s!", p_iam, p_var)

# Entry point:
reset
iam = "dv2524-gnu/histogramsstacked.gnu"
print sprintf("%s: Enter...", iam)
if(!exists("arg_output")) { # Optional arguments.
	arg_output = "default.ps"
	print default(iam, arg_output)
}
if(!exists("arg_terminal")) {
	arg_terminal = "postscript"
	print default(iam, arg_terminal)
}
plots_notitle = 0
if(!exists("arg_title1")||!exists("arg_title2")||!exists("arg_title3")) {
	plots_notitle = 1
}
if(!exists("arg_data1")||!exists("arg_data2")||!exists("arg_data3")) { # Mandatory arguments.
	print usage(iam)
	pause -1 p
}

set terminal arg_terminal size 10cm, 15cm
set output arg_output

set multiplot layout 3,1

plots_bin_num = 100
plots_bin_min = 1000 # Should the bins really be integer precision?
plots_bin_max = 0
plots_data_min = 1000.0
plots_data_max = 0.0

# Common settings:
unset xtics
unset ytics
set tmargin 0
set bmargin 0    

files=sprintf("%s %s %s", arg_data1, arg_data2, arg_data3)
do for [i=1:words(files)] {
    arg_data = word(files, i)

    stats arg_data name "data" nooutput

    hist_data_mean = data_mean_y
    hist_data_min = hist_data_mean - data_stddev_y
    hist_data_max = hist_data_mean + data_stddev_y
    hist_binMin = floor(max(hist_data_min, data_min_y)) # Currently causes bins to be rendered with differing widths, for some reason.
    hist_binMax = ceil(min(hist_data_max, data_max_y))

    plots_bin_min = min(hist_binMin, plots_bin_min) # Integer precision
    plots_bin_max = max(hist_binMax, plots_bin_max)
    plots_data_min = min(hist_data_min, plots_data_min) # Floating point precision
    plots_data_max = max(hist_data_max, plots_data_max)
}

	plots_bin_width = (plots_data_max - plots_data_min) / plots_bin_num

    set style fill solid 0.5 # Fill bins to make them gorgous.
    set offset graph 0.05, 0.05, 0.05, 0.0 # Correct erronously rendered bins.
    set boxwidth plots_bin_width # Avoid incorrectly rendering empty bins. (http://stackoverflow.com/questions/2471884/histogram-using-gnuplot)

    set xrange [plots_bin_min:plots_bin_max]
    set yrange [0:]

do for [i=1:words(files)] {
	arg_data = word(files, i)
	if(i==3) {
		set xtics nomirror
		set bmargin 1 # Extra spacing for figure description (I'm a generous God).
	}
	if(plots_notitle==0) {
		titles=sprintf("%s %s %s", arg_title1, arg_title2, arg_title3)
		set title word(titles, i) offset -25,-8,0 # Hack
	}

    stats arg_data name "data" nooutput # To retrieve data_records.

    plot arg_data u (mapToBin($1, plots_bin_width, plots_bin_min)):(100.0/data_records) smooth freq w boxes lc rgb"black" notitle
}

unset multiplot

print sprintf("%s: Exit.", iam)