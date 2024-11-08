#!/usr/bin/env python3

def famous_births(vdict:dict):
    ldict=list(vdict.values())
    sortedlist = sorted(ldict , key=lambda elem: elem['date_of_birth'])
    for i in sortedlist:
        print(f"{i['name']} is a great scientist born in {i['date_of_birth']}.")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)