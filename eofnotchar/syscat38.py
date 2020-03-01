# syscat38.py
import sys
import os

fd = os.open(sys.argv[1], os.O_RDONLY)

while c := os.read(fd, 1):
    os.write(sys.stdout.fileno(), c)
