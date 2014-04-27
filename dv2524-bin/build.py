#!/bin/python
# Script deleting all contents (apart from itself) in dv2524-bin/ directory.

import os

g_iam = "dv2524-bin/build.py"

g_cleanfiletypes = [".aux", ".bbl", ".blg", ".log", ".out", ".bib", ".bst", ".sty", ".cls", ".toc", ".pdf", ".gin", ".glo", ".acn", ".acr", ".alg", ".glg", ".gls", ".ist", ".ind", ".ilg", ".idx", ".tex", ".txt", ".svg"]
g_cleaninadditionto = ["README",]
g_cleanexcept = ["build.py", "README.md§"]

def clean(p_from):
    for ftype in g_cleanfiletypes:
        filesoftype = [f for f in os.listdir(".") if f.endswith(ftype) or f in g_cleaninadditionto]
        print(p_from + ": Deleting " + str(len(filesoftype)) + " instances of filetype " + ftype + " from build directory...")
        for f in filesoftype:
            if str(f) not in g_cleanexcept:
                os.remove(f)

# Entry point:
print(g_iam + ": Enter...")

clean(g_iam) # Nuke from orbit.

print(g_iam + ": Exit.")
