#!/usr/bin/env python3

number = input("Enter a number ")
if number.isdigit():
    if int(number) < 100:
        print("The number is less than 100")
    else:
        print("the number is invalid")  
else:
    print("That is not a number ")          

print("will always print")