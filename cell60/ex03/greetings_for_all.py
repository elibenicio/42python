#!/usr/bin/env python3

def greetings(firstname="noble stranger."):
    if isinstance(firstname, str):
        print(f"Hello, {firstname}.")
    else:
        print("Error! It was not a name.")

greetings('Elisangela') 
greetings('Bruno')     
greetings()
greetings(5)