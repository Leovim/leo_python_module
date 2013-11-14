#coding=utf8
import sys

def convert_to_hex():
    """ convert one or more arguments from decimal to hex """
    print sys.argv
    args = sys.argv
    del args[0]
    for num in args:
        print hex(int(num))

convert_to_hex()
