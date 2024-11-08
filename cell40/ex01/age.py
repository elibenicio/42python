#!/usr/bin/env python3
intAge=input("Please tell me your age: ")
print("You are currently",str(intAge),"years old.")
intSoma=10
cont=0
while cont<3:
    intAge=int(intAge)+10
    print("In",str(intSoma),"years, you'll be",str(intAge),"years old.")
    intSoma=intSoma+10
    cont=cont+1