# histograms.gnu
# GNUplot script creating a 2x3 figure of histograms.
# Requires GNUplot 4.6 or later.
# ---
# Arguments:
# 1. Data set #1 : arg_data1
# 2. Data set #2 : arg_data2
# 3. Data set #3 : arg_data3
# 4. Data set #4 : arg_data4
# 5. Data set #5 : arg_data5
# 6. Data set #6 : arg_data6
# 7. Out Terminal : arg_terminal
# 7. Out Filename : arg_output
# ---

min(p_x, p_y) = (p_x<p_y) ? p_x : p_y
max(p_x, p_y) = (p_x>p_y) ? p_x : p_y
mapToBin(p_x, p_binWidth, p_binMin) = p_binWidth * (floor((p_x - p_binMin) / p_binWidth) + 0.5) + p_binMin # http://stackoverflow.com/a/19596160
usage(p_iam) = sprintf("%s: Usage: gnuplot -e \"arg_data1-6='data.dat';arg_terminal='type';arg_output='filename.type'\" histogram.gnu", p_iam)
press(p_iam) = sprintf("%s: Press any key to continue.", p_iam)
default(p_iam, p_var) = sprint("%s: Warning, using default var: %s!", p_iam, p_var)

# Entry point:
reset
iam = "dv2524-gnu/histograms.gnu"
print sprintf("%s: Enter...", iam)
if(!exists("arg_output")) { # Optional arguments.
    arg_output = "default.ps"
    default(iam, arg_output)
}
if(!exists("arg_terminal")) {
    arg_terminal = "postscript"
    default(iam, arg_terminal)
}
if(!exists("arg_data1")||!exists("arg_data2")||!exists("arg_data3")||!exists("arg_data4")||!exists("arg_data5")||!exists("arg_data6")) { # Mandatory arguments.
    print usage(iam)
    pause -1 press(iam) # We should abort script here rather than simply pause it.
}

set terminal arg_terminal size 20cm,15cm
set output arg_output

set multiplot layout 3,2

files=sprintf("%s %s %s %s %s %s", arg_data1, arg_data2, arg_data3, arg_data4, arg_data5, arg_data6)

do for [i=1:words(files)] {
    arg_data = word(files, i)

    stats arg_data name "data"

    hist_numBins = 100
    hist_data_mean = data_mean_y
    hist_data_min = hist_data_mean - data_stddev_y
    hist_data_max = hist_data_mean + data_stddev_y
    hist_binWidth = (hist_data_max - hist_data_min) / hist_numBins
    hist_binMin = floor(max(hist_data_min, data_min_y)) # Currently causes bins to be rendered with differing widths, for some reason.
    hist_binMax = ceil(min(hist_data_max, data_max_y))

    set xrange [hist_binMin:hist_binMax]
    set yrange [0:]
    #tics = floor((hist_binMax-hist_binMin)/5)
    #set xtics tics
    #set xtics hist_binMin, tics, hist_binMax

    set boxwidth hist_binWidth # Avoid incorrectly rendering empty bins. (http://stackoverflow.com/questions/2471884/histogram-using-gnuplot)
    set style fill solid 0.5 # Fill bins to make them gorgous.
    set offset graph 0.05, 0.05, 0.05, 0.0 # Correct erronously rendered bins.

    plot arg_data u (mapToBin($1, hist_binWidth, hist_binMin)):(100.0/data_records) smooth freq w boxes lc rgb"black" notitle
}

unset multiplot

print sprintf("%s: Exit.", iam)

# Canvas size:
#set key default
#set key box
#set multiplot layout 3,2
#set key at screen 0.75, 0.25

# Labels:
#set xlabel "Frametime (ms)"
#set ylabel "Sample frequency"
