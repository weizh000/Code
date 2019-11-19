#!/usr/bin/env python3

import sys

dict1 = {}
for argv in sys.argv[1:]:
    id,name = argv.split(':')
    dict1[id] = name

for k,v in dict1.items():
    print('ID:{} Name:{}'.format(k,v))
