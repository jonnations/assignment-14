#!/usr/bin/env python
# encoding: utf-8

"""
My 2nd program for Assignment 14

Created by Michael Henson on 14 March 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import argparse
import glob
import os
import shutil


def askingforfiles():
    parser = argparse.ArgumentParser(
        description="Asking User to Provide the path to the directory for task1 ")
    parser.add_argument(
        "--input",
        required=True,
        help="Provide the the directory path to task1 ",
        type=str
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Provide the output directory path",
        type=str
    )
    return parser.parse_args()


# def makedirectory(string):
#    newpath = os.path.join(string, 'newfile')
#    print(newpath)
#    if not os.path.exists(newpath):
#        os.makedirs(newpath)
#    return newpath


def main():
    path = askingforfiles()
    #name = makedirectory(path.input)
    my_files = glob.glob(os.path.join(path.input, "*.fastq"))
    for filename in my_files:
        if os.path.exists(path.output) is False:
            print("\n Create this directory before you run this")
        else:
            shutil.copy(filename, path.output)


if __name__ == '__main__':
    main()
