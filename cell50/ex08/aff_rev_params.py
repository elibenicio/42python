#!/usr/bin/env python3

import sys

if len(sys.argv)==1:
    print('none')
else:
    param = sys.argv[1:]
    for i in reversed(param):
        print(i)