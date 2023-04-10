#!/usr/bin/env python3

import os

print(os.getcwd())
os.rename("first.txt", "second.txt")
os.system('ls')
os.system('./script.py')


