# histogram.gnu
# GNUplot script rendering a histogram based on a lone data file.
# Requires GNUplot 4.6 or later.
# ---
# Arguments:
# 1. Data set		: arg_data
# 2. Output file	: arg_output
# ---
# Invoke accordingly:
# gnuplot -e "arg_data='results/paraphong1448x1448.ms';arg_output='out.svg'" histogram.gnu

# Utility methods:
usage(p_iam) = sprintf("%s: Usage: gnuplot -e \"arg_data='results/paraphong1448x1448.ms';arg_output='out.svg'\" histogram.gnu", p_iam)
press(p_iam) = sprintf("%s: Press any key to continue.", p_iam)

min(p_x, p_y) = (p_x<p_y) ? p_x : p_y
max(p_x, p_y) = (p_x>p_y) ? p_x : p_y
mapToBin(p_x, p_binWidth, p_binMin) = p_binWidth * (floor((p_x - p_binMin) / p_binWidth) + 0.5) + p_binMin # http://stackoverflow.com/a/19596160

# Entry point:
reset
iam = "dv2524-gnu/histogram.gnu"
print sprintf("%s: Enter...", iam)

if(!exists("arg_output")) { # Optional arguments.
	arg_output = "default.svg"
}
if(!exists("arg_data")) { # Mandatory arguments.
	print usage(iam)
	pause -1 press(iam) # We should abort script here rather than simply pause it.
}

set terminal svg # Should be customizable.
set output arg_output
set xlabel "Frametime (ms)"
set ylabel "Sample frequency"

print sprintf("%s stats:", arg_data)
stats arg_data name "data"

hist_numBins = 250
hist_data_mean = data_mean_y
hist_data_min = hist_data_mean - data_stddev_y
hist_data_max = hist_data_mean + data_stddev_y
hist_binWidth = (hist_data_max - hist_data_min) / hist_numBins
hist_binMin = floor(max(hist_data_min, data_min_y)) # Currently causes bins to be rendered with differing widths, for some reason.
hist_binMax = ceil(min(hist_data_max, data_max_y))

set xrange [hist_binMin:hist_binMax]
set yrange [0:]
set boxwidth hist_binWidth # Avoid incorrectly rendering empty bins. (http://stackoverflow.com/questions/2471884/histogram-using-gnuplot)
set style fill solid 0.5 # Fill bins to make them gorgous.
set offset graph 0.05, 0.05, 0.05, 0.0 # Correct erronously rendered bins.

plot arg_data u (mapToBin($1, hist_binWidth, hist_binMin)):(1.0) smooth freq w boxes lc rgb"black" notitle

print sprintf("%s: Exit.", iam)

# ---

# Insert to remove axis ticks on the right-/top axes:
# set tics out nomirror

# Insert to display increased precision in axes:
#set xtics hist_binMin, (hist_binMax - hist_binMin) / 5, hist_binMax
