#!/bin/bash

# Clean
for file in *.aux *.bbl *.blg *.log *.bib *.nav *.out *.snm *.toc ; do # .bib files are generated each run, so remove old ones to avoid Lovecraftian bugs.
	rm $file
done

# Create original bib-files containing desired entries:
# Said entries are copied into files with an additional '.bib' appended to the filename (in case the user is building on my Windows-machine using MiKTeX).
touch proposalbibliography.bib proposalbibliography.bib.bib
cat ../dv2524-bib/papers.bib ../dv2524-bib/magazines.bib ../dv2524-bib/dissertations.bib ../dv2524-bib/inproceedings.bib ../dv2524-bib/journals.bib ../dv2524-bib/publications.bib > proposalbibliography.bib
cat proposalbibliography.bib > proposalbibliography.bib.bib
touch proposalreferences.bib proposalreferences.bib.bib
cat ../dv2524-bib/technicaldocs.bib ../dv2524-bib/web.bib > proposalreferences.bib
cat proposalreferences.bib > proposalreferences.bib.bib

# Build .aux-files and symbol tree
pdflatex proposal

# Build bibliography
for file in *.aux ; do
	bibtex $file
done

# Build with compiled bibliography entries. ...Twice (because of reasons).
pdflatex proposal
pdflatex proposal

# Open in pdf reader (TODO: use system pdf-reader)
evince proposal.pdf # Remove me!
