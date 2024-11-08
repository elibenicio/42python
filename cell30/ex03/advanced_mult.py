#!/usr/bin/env python3

import sys

if len(sys.argv)>1:
    print("none")
else:
    cont=0
    intMult=0
    intOper=0
    strTable=""
    while intMult<=10:
        while cont<=10:
            strTable=strTable+" "+str(intOper)
            intOper=intOper+intMult
            cont=cont+1

        print("Table de "+str(intMult)+": "+strTable)
        intMult=intMult+1
        cont=0
        intOper=0
        strTable=""

