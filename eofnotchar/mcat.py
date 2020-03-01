# mcat.py
import sys

with open(sys.argv[1]) as fin:
    while True:
        c = fin.read(1) # read max 1 char
        if c == '':     # EOF
            break
        print(c, end='')
