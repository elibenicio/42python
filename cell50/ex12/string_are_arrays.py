#!/usr/bin/env python3

import sys
import re

imprime=''

if len(sys.argv)!=2:
    print('none')
elif len(re.findall('z',sys.argv[1]))==0:
    print('none')
else:
    for i in sys.argv[1]:
        if i=='z':
            imprime=imprime+'z'
    print(imprime)