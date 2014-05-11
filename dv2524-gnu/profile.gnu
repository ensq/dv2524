# profile.gnu
# GNUplot script the purpose of which is to visualize error data in profiling of Simics platforms.
# ---
# Arguments:
# 1. Data set #1 : arg_data
# 7. Out Terminal : arg_terminal
# 7. Out Filename : arg_output
# ---

usage(p_iam) = sprintf("%s: Usage: gnuplot -e \"arg_data='data.dat';arg_terminal='type';arg_output='filename.type'\" profile.gnu", p_iam)
press(p_iam) = sprintf("%s: Press any key to continue.", p_iam)
default(p_iam, p_var) = sprint("%s: Warning, using default var: %s!", p_iam, p_var)

# Entry point:
reset
iam = "dv2524-gnu/profile.gnu"
print sprintf("%s: Enter...", iam)
if(!exists("arg_output")) { # Optional arguments.
    arg_output = "default.tex"
    default(iam, arg_output)
}
if(!exists("arg_terminal")) {
    arg_terminal = "epslatex"
    default(iam, arg_terminal)
}
#if(!exists("arg_data")) { # Mandatory arguments.
#    print usage(iam)
#    pause -1 press(iam) # We should abort script here rather than simply pause it.
#}

set terminal postscript #arg_terminal
set output "profile.ps" #arg_output

f(x) = mean_y
fit f(x) arg_data u 0:1 via mean_y

stats arg_data name "data"
min_y = data_min_y
max_y = data_max_y

stddev_y = sqrt(FIT_WSSR / (FIT_NDF + 1))

set label 1 gprintf("Mean = %g", mean_y) at 2, min_y-0.2
set label 2 gprintf("Standard deviation = %g", stddev_y) at 2, min_y-0.35
plot mean_y-stddev_y with filledcurves y1=mean_y lt 1 lc rgb "#bbbbdd", \
mean_y+stddev_y with filledcurves y1=mean_y lt 1 lc rgb "#bbbbdd", \
mean_y w l lt 3, arg_data u 0:1 w p pt 7 lt 1 ps 1

print sprintf("%s: Exit.", iam)
