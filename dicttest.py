#!/usr/bin/env python3

import sys
'''
dict1 = {}
for argv in sys.argv[1:]:
    id,name = argv.split(':')
    dict1[id] = name
'''
output_dict = {}
def handle_data(arg_):
    i,name = arg_.split(':')
    output_dict[i] = name

def print_data(k,v):
    print('ID:{} Name:{}'.format(k,v))

'''
for k,v in dict1.items():
    print('ID:{} Name:{}'.format(k,v))
'''

if __name__ == '__main__':
    
    for arg in sys.argv[1:]:
        handle_data(arg)
    
    for key in output_dict:
        print_data(key,output_dict[key])

