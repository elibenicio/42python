#!/usr/bin/env python3

import sys
#arrNames=[]

def filter_func(value):
    #print(value)
    name,color=value
    #vai retorna verdadeiro/falso
    return color=="red"

def find_the_redheads(vdict:dict):
    #print(vdict)
    #print(vdict.keys())
    #print(vdict.values())
    #print(vdict.items())
    arrNames = dict(filter(filter_func,vdict.items())).keys()

    return list(arrNames)
    #for key, value in vdict.items():
    #    if value=="red":
    #        arrNames.append(f"{key.capitalize()}")
    #return arrNames

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))


#list_from_dict = list(sample_dict.items())