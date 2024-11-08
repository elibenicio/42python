#!/usr/bin/env python3
texto=input("What you gotta say? : ")
while texto or texto=='':
    texto=input("I got that! Anithing else? : ")
    if texto=="STOP":
        break
