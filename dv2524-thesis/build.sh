#!/bin/bash

# Clean:
for file in *.aux *.bbl *.blg *.log *.out ; do
	rm $file
done

# Copy required packages to bin:
cp ../dv2524-packages/gitinfo/gitinfo.sty gitinfo.sty
cp ../dv2524-packages/gitinfo/gitsetinfo.sty gitsetinfo.sty

pdflatex thesis
pdflatex thesis