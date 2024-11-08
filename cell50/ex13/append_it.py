#!/usr/bin/env python3

import sys
from re import match

if len(sys.argv)==1:
    print('none')
else:
    arrArg=sys.argv[1:]
    for i in arrArg:
        #print(match(r".*ism$", i))
        if match(r".*ism$", i)==None: print(i+"ism")