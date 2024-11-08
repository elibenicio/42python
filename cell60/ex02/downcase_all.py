#!/usr/bin/env python3

import sys

def downcase_all(arrArg):
    for i in arrArg:
        print(i.lower())

if len(sys.argv)<2:
    print('none')
else:
    arrArg=sys.argv[1:]
    downcase_all(arrArg)