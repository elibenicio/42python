#!/usr/bin/env python3

import sys
import numpy as np

arrSeq=[]
i=0

if len(sys.argv)==1:
    print('none')
else:
    start_value=int(sys.argv[1])
    stop_value=int(sys.argv[2])
    arrSeq=np.arange(start_value, stop_value+1)
    print(arrSeq)