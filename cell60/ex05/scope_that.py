#!/usr/bin/env python3

def add_one(varAdd:int):
    return varAdd+1

value=2

print(value)

add_one(value)

print(add_one(value))
print(value)

value=add_one(value)
print(value)