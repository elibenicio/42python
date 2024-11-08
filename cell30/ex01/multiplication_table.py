#!/usr/bin/env python3
print("Enter a number")
intNum=int(input())
intMult=0
while intMult<=9:
    intRes=intMult*intNum
    print(str(intMult)+" x "+str(intNum)+" = "+str(intRes))
    intMult=intMult+1

