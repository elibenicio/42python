#!/usr/bin/env python3

import sys
import numpy as np

arrArg=np.array (sys.argv)

if len(sys.argv)<2:
    print('none')
else:
    print('parameters:',len(sys.argv)-1)
    for i in range(arrArg.size):
        if i>0:
            print(f'{arrArg[i]}: {len(arrArg[i])}')
