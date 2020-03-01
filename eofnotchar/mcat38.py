# mcat38.py
import sys

with open(sys.argv[1]) as fin:
    while (c := fin.read(1)) != '':  # read max 1 char at a time until EOF
        print(c, end='')
