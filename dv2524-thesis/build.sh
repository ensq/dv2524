#!/bin/bash
clear
printf "dv2524-thesis/build.sh\n"
printf "---\n\n"

# Clean:
printf "Cleaning...\n"
for file in *.aux *.bbl *.blg *.log *.out ; do
	rm $file
done

# Unzip packages
printf "Uncompressing...\n"
unzip -o ../dv2524-packages/gitinfo.zip -d ../dv2524-packages
unzip -o ../dv2524-encl/dv2524-encl.zip -d ../dv2524-encl

# Move files into build directory:
printf "Copying files into build directory...\n"
cp ../dv2524-packages/gitinfo/gitinfo.sty gitinfo.sty
cp ../dv2524-packages/gitinfo/gitsetinfo.sty gitsetinfo.sty

printf "Building LaTeX-document with pdflatex...\n"
pdflatex thesis
pdflatex thesis

# evince thesis.pdf
