#!/usr/bin/env python3
print("Enter the first number:")
fnumber=int(input())
print("Enter the second number:")
snumber=int(input())
result=fnumber * snumber
if result>0:
    print(str(fnumber) + " x " + str(snumber) + " = " + str(result))
    print("The result is positive.")
elif result<0:
    print(str(fnumber) + " x " + str(snumber) + " = " + str(result))
    print("The result is negative.")
else:
    print(str(fnumber) + " x " + str(snumber) + " = " + str(result))
    print("The result is positive and negative.")
