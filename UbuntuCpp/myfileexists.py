#!/usr/bin/env python3

import os

os.system('ls -l')

file = input("Enter a file name: ")

if os.path.isfile(file):
    print("The file exists")
else:
    print("the file does not exist")
    print("Creating " + file + "...")
    os.system('touch {}'.format(file))