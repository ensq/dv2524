#!/bin/bash

# Clean
for file in *.aux *.bbl *.blg *.log *.out ; do
	rm $file
done

pdflatex thesis
pdflatex thesis