#!/usr/bin/env python

fname = 'webpage_refs.bib'

omits = ['file =', 'owner =', 'copyright', 'shorttitle =', 'note =', 'bibtex[']

with open(fname) as f:
    lines = f.readlines()
    cleaned_lines = [line for line in lines if not any(omit in line for omit in omits)]


# probably not super smart to delete the bibfile in case of exceptions, but
# then again it's only a bibfile
import os
os.remove(fname)

with open(fname, 'w') as f:
    f.writelines(cleaned_lines)
