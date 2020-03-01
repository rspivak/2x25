# syscat.py
import sys
import os

fd = os.open(sys.argv[1], os.O_RDONLY)

while True:
    c = os.read(fd, 1)
    if not c:  # EOF
        break
    os.write(sys.stdout.fileno(), c)
