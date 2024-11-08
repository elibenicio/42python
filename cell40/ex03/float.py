#!/usr/bin/env python3
num=input("Give me a number:")

fnum=float(num)

if fnum.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
