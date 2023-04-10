#!/usr/bin/env python3

myFile = "file.txt"
try:
    file = open(myFile, "a")        #  r read only  a is for append
except FileNotFoundError as e:
    print("Error opening " + myFile + "\n\n")
    print(e)
    exit(1)

movies = ["The Matrix", "The Lord Of The Rings", "The Avengers"]

for m in movies:
    file.write(m + "\n")
file.close()
