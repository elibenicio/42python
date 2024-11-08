#!/usr/bin/env python3

import sys

def shrink(strSlice:str):
    return strSlice[slice(8)]

def enlarge(strEnlarge:str):
    while len(strEnlarge)<8:
        strEnlarge=strEnlarge + 'x'
    return strEnlarge

if len(sys.argv)==1:
    print('none')
else:
    arrArg=sys.argv[1:]
    for i in arrArg:
        if len(i)==8:
            print(i)
        elif len(i)<8:
            print(enlarge(i))
        else:
            print(shrink(i))
