# histogram2x3.gnu
# GNUplot script creating a 2x3 figure of histograms.

min(p_x, p_y) = (p_x<p_y) ? p_x : p_y
max(p_x, p_y) = (p_x>p_y) ? p_x : p_y
mapToBin(p_x, p_binWidth, p_binMin) = p_binWidth * (floor((p_x - p_binMin) / p_binWidth) + 0.5) + p_binMin # http://stackoverflow.com/a/19596160

# Entry point:
reset
set terminal postscript
set output "histogram2x3.ps"

#set xlabel "Frametime (ms)"
#set ylabel "Sample frequency"

#set key default
#set key box
set multiplot layout 3,2
#set key at screen 0.75, 0.25

files = "results/simicsjulia225.ms results/parajulia225.ms results/simicsjulia450.ms results/parajulia450.ms results/simicsjulia900.ms results/parajulia900.ms"

do for [i=1:words(files)] {
    arg_data = word(files, i)

    stats arg_data name "data"

    hist_numBins = 250
    hist_data_mean = data_mean_y
    hist_data_min = hist_data_mean - data_stddev_y
    hist_data_max = hist_data_mean + data_stddev_y
    hist_binWidth = (hist_data_max - hist_data_min) / hist_numBins
    hist_binMin = floor(max(hist_data_min, data_min_y)) # Currently causes bins to be rendered with differing widths, for some reason.
    hist_binMax = ceil(min(hist_data_max, data_max_y))

    #tics = (hist_binMax-hist_binMin)/5
    #set xtics hist_binMin, tics, hist_binMax

    set xrange [hist_binMin:hist_binMax]
    set yrange [0:]
    set boxwidth hist_binWidth # Avoid incorrectly rendering empty bins. (http://stackoverflow.com/questions/2471884/histogram-using-gnuplot)
    set style fill solid 0.5 # Fill bins to make them gorgous.
    set offset graph 0.05, 0.05, 0.05, 0.0 # Correct erronously rendered bins.

    plot arg_data u (mapToBin($1, hist_binWidth, hist_binMin)):(100.0/data_records) smooth freq w boxes lc rgb"black" notitle
}

unset multiplot
