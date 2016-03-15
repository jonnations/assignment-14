#!/usr/bin/env python
# encoding: utf-8

"""
My 1st program for Assignment 14

Created by Michael Henson on 14 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import argparse
import os
import glob
import re
from collections import Counter

def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Asking User to Provide the path to the directory for task1 ")
    parser.add_argument(
        "--input",
        required=True,
        help="Provide the the directory path to task1 ",
        type=str
    )
    return parser.parse_args()


def chapter1clean(string):
    list = re.findall(
                "[a-zA-Z]+[-][a-zA-Z]+|[a-zA-z]+['][a-zA-Z]+|[a-zA-Z]+",
                string)
    #https://docs.python.org/2/library/re.html
    '''
    this took me forever to figure out and what to use
    since I previous got this wrong. this seems simple compared
    to previous attempted to break apart using string
    '''
    '''
    http://stackoverflow.com/questions/10134372/get-a-list-of-names-which-start-with-certain-letters
    First answer helped tell me how to put together a list comprehension.
    '''
    my_dict = [str.lower(word) for word in list]
    numbers = Counter(my_dict)
    return numbers


def chapter1unique(string):
    uniques = set(string)
    return uniques


def total_counts(string):
    counters = len(string.split())
    return counters



def main():
    path = askingforfiles()
    my_files = glob.glob(os.path.join(path.input, "*.txt"))
    with open(my_files[0], 'r') as file1:
        read1 = file1.read()
        clean1 = chapter1clean(read1)
        total1 = total_counts(read1)
        unique1 = chapter1unique(clean1)
    print('\nWhat is the total count in Ch1\n')
    print(total1)
    print('\nWhat is the number of uniques in Ch1\n')
    print(len(unique1))
    with open(my_files[1], 'r') as file2:
        read2 = file2.read()
        clean2 = chapter1clean(read2)
        total2 = total_counts(read2)
        unique2 = chapter1unique(clean2)
    print('\nWhat is the total count in Ch2\n')
    print(total2)
    print('\nWhat is the number of uniques in Ch2\n')
    print(len(unique2))
    shared = set(clean1).intersection(set(clean2))
    print('\n How many shared?\n')
    print(len(shared))
    print('\n How many unique to 1?\n')
    dif1 = set(clean1).difference(set(clean2))
    print(len(dif1))
    print('\n How many unique to 2?\n')
    dif2 = set(clean2).difference(set(clean1))
    print(len(dif2))

if __name__ == '__main__':
    main()
