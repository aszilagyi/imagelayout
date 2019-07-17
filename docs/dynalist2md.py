#!/usr/bin/env python3

'''convert dynalist asterisk-marked text export to markdown'''

import sys

f = open(sys.argv[1])
txt = f.read()
f.close()

# replace __ by _ except inside `...`

t = []
inbacktick = False
_count = 0
for c in txt:
    if c != '_':
        _count = 0
    if c == '`':
        inbacktick = not inbacktick
    if inbacktick:
        t += c
        continue
    if c == '_':
        _count += 1
        if _count == 2:
            _count = 0
            continue
    t += c

# replace `...` by ```...``` if there is a line break inside

inbacktick = False
lbr = False
for x in range(len(t)):
    if t[x] == '\n':
        lbr = True
    if t[x] == '`':
        inbacktick = not inbacktick
        if inbacktick:
            xopenbacktick = x
            lbr = False
        else:
            if lbr:
                t[xopenbacktick] = '\n```\n'
                t[x] = '\n```\n'
txt = ''.join(t)

# convert first bullet point to title, dedent rest of the file

lines = txt.splitlines()

lines[0] = '## '+lines[0].split(maxsplit=1)[1]
for j in range(1, len(lines)):
    if lines[j].strip().startswith('* ') or lines[j-1].strip().startswith('* '):
        lines[j] = lines[j][4:]

# put leading spaces at the start of extra note lines


for j in range(1, len(lines)):
    line = lines[j]
    if not line.strip().startswith('* '):
        if lines[j-1].strip().startswith('* '):
            nspaces = len(line)-len(line.lstrip())
        else:
            lines[j] = ' '*nspaces+line
        

# put \ to end of first line of bulletpoints


for j, line in enumerate(lines):
    if (j < len(lines)-1 and line.strip().startswith('* ') and 
      not lines[j+1].strip().startswith('* ')):
        print(line+'\\')
    else:
        print(line)
