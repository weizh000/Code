#!/usr/bin/nev python3

def char_count(str_):
    char_list = set(str_)
    print(char_list)
#    for char in char_list:
#        print(char, str_.count(char))

if __name__ == '__main__':

    s = input("Enter a string:")

    char_count(s)
