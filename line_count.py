#coding=utf8
'''
File: line_count.py
Author: Leo_vim
Description: 
    '''

import sys
import os

suffix_list = ['.html', '.xml', '.css', '.js', '.php', '.py', '.rb', '.c',
               '.cpp', '.java', '.cs', '.sh', '.h', '.hs']

def linecount(filename):
    """get a Filename and print the line number of the file"""
    count = 0
    for line in open(filename):
        if(line != '\n'):
            count += 1
            return count

def filecount(dirname):
    if os.path.isdir(dirname) is True:
        filelist = os.listdir(dirname)
        line_number = traversal(filelist, dirname)
    else:
        line_number = linecount(dirname)
        return line_number

def traversal(filelist, dirname):
    total_number = 0
    for subname in filelist:
        subname = dirname + subname
        if os.path.isdir(subname) is not True:
            suffix = os.path.splitext(subname)
            if suffix[1] in suffix_list:
                print subname
                line_number = linecount(subname)
                print line_number
                total_number += int(line_number)
            else:
                continue
        else:
            subname = subname + '/'
            line_number = filecount(subname)
            total_number += int(line_number)
            return total_number

def main():
    dirname = raw_input('Please input a dirname')
    print 'The dir name is',dirname
    line_number = filecount(dirname)
    print 'count complete!'
    print ''
    print line_number

main()
