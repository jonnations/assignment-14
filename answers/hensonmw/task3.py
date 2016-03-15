#!/usr/bin/env python
# encoding: utf-8

"""
My 3rd program for Assignment 14

Created by Michael Henson on 14 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import argparse
import glob
import os


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


def getfile(file2, my_list):
    with open(file2, 'r') as file1:
            file3 = file1.read()
            file4 = file3.split(' ')
            loads = (int(digit) for digit in file4)
            my_list.append(loads)
            return my_list


def main():
    path = askingforfiles()
    my_files = glob.glob(os.path.join(path.input, "*.txt"))
    my_list = []
    for x in my_files:
        my_list = getfile(x, my_list)
    print(my_list)
    results = map(sum, my_list)
    print(results)
    print(sum(results))


if __name__ == '__main__':
    main()
