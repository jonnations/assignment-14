


## Task 1

There are 2 chapters of Darwin's Origin of Species in this repository within a directory entitled `task1-files`.  Write a program that uses `argparse` and `glob` to open and read these chapters and some other code to get a list of all words in each chapter.  Then output, to the command line, a pretty-printed list of the following:

* the total count of words in Chapter 1
* the count of unique words in Chapter 1
* the total count of words in Chapter 2
* the count of unique words in Chapter 2
* the count of words in Chapter 1 that ARE in Chapter 2
* the count of words in Chapter 1 that ARE NOT in Chapter 2
* the count of words in Chapter 2 that ARE NOT in Chapter 1

Your program should contain a main loop and an ifmain statement, it should be formatted correctly, and you should be sure to use argparse to `argparse` and `glob` to read in the chapter files.

- [ ] Program is correctly formatted (0.5 pt)
- [ ] Program includes `main()` function and "ifmain" statement (0.5 pt)
- [ ] Program uses `argparse` and `glob` (1.0 pt)
- [ ] Program functions as requested (3.0 pt)

## Task 2

In the directory `task2-files`, there are a lot of files.  Write a program that uses `argparse`, `glob`, and `os` to copy **only** the fastq files to a new directory.  Your program should contain a main loop and an ifmain statement, it should be formatted correctly, and you should take both the input directory containing the files you want to copy and the output directory where you will copy the files as arguments on the command-line.

- [ ] Program is correctly formatted (0.5 pt)
- [ ] Program includes `main()` function and "ifmain" statement (0.5 pt)
- [ ] Program uses `argparse`, `glob`, and `os` (2.0 pt)
- [ ] Program functions as requested (2.0 pt)

## Task 3

In the directory `task3-files` there are 10 files, each containing a random selection of integer values.  Using a combination of `argparse` and `glob`, read these files.  Then, use `map` to compute the sum of all integer values across all files. Your program should contain a main loop and an ifmain statement, and it should be formatted correctly.

- [ ] Program is correctly formatted (0.5 pt)
- [ ] Program includes `main()` function and "ifmain" statement (0.5 pt)
- [ ] Program uses `argparse`, `glob` (0.5 pt)
- [ ] Program uses `map` (2.0 pt)
- [ ] Program functions as requested (1.5 pt)
