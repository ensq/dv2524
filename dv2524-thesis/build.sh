#!/bin/bash
# Script building thesis document.
# ---
# Note that build.sh treats some files as temporary ones (deleted prior to- and after each build) that may not be considered such by the user.
# Such a file is .bib, which is compiled by the script from an assortment of .bib-files in the dv2524-bib/ directory.
# ---

clear
printf "dv2524-thesis/build.sh\n"
printf "---\n\n"

# Clean:
printf "Cleaning...\n"
for file in *.aux *.bbl *.blg *.log *.out *.bib; do
	rm $file
done

# Unzip packages
printf "Uncompressing...\n"
unzip -o ../dv2524-packages/gitinfo.zip -d ../dv2524-packages
unzip -o ../dv2524-encl/dv2524-encl.zip -d ../dv2524-encl

# Create original bib-files containing desired entries:
# Said entries are copied into files with an additional '.bib' appended to the filename (in case the user is building on my Windows-machine using MiKTeX).
touch thesisbibliography.bib thesisbibliography.bib.bib
cat ../dv2524-bib/papers.bib ../dv2524-bib/magazines.bib ../dv2524-bib/dissertations.bib ../dv2524-bib/inproceedings.bib ../dv2524-bib/journals.bib ../dv2524-bib/publications.bib > thesisbibliography.bib
cat thesisbibliography.bib > thesisbibliography.bib.bib
touch thesiswebreferences.bib thesiswebreferences.bib.bib
cat ../dv2524-bib/technicaldocs.bib ../dv2524-bib/web.bib > thesiswebreferences.bib
cat thesiswebreferences.bib > thesiswebreferences.bib.bib

# Move files into build directory:
printf "Copying files into build directory...\n"
cp ../dv2524-packages/gitinfo/gitinfo.sty gitinfo.sty
cp ../dv2524-packages/gitinfo/gitsetinfo.sty gitsetinfo.sty

printf "Building LaTeX-document with pdflatex...\n"
# Build intermediate .aux-files and symbol tree:
pdflatex thesis

# Build [multibib] bibliography:
bibtex bib.aux
bibtex ref.aux

pdflatex thesis
pdflatex thesis

# Cleaning again:
printf "Cleaning again...\n"
for file in *.aux *.bbl *.blg *.log *.out *.bib ; do
	rm $file
done

# evince thesis.pdf
