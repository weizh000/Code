#!/usr/bin/env python3

import sys 

s1 = []
s2 = []
for argv in sys.argv:
    if len(argv) > 3:
        s1.append(argv)
    else:
        s2.append(argv)
print(s1)
print(s2)
