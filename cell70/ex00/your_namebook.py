#!/usr/bin/env python3

import sys
arrNames=[]

def array_of_names(vdict:dict):
    for key, value in vdict.items():
        arrNames.append(f"{key.capitalize()} {value.capitalize()}")
    return arrNames

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))