# list_of_dictionaries_show_all_pprint.py

from pprint import pprint

people = [
    { 
        'firstName' : 'John', 
        'lastName' : 'Rambo', 
        'dob' : '3-1-1977', 
        'weight' : '170'
    },
    { 
        'firstName' : 'Jesse', 
        'lastName' : 'Tomson', 
        'dob' : '1-8-1978', 
        'weight' : '185'
    }
]

pprint(people)

input("Press Enter to Exit")

'''
[{'dob': '3-1-1977', 'firstName': 'John', 'lastName': 'Rambo', 'weight': '170'},
 {'dob': '1-8-1978',
  'firstName': 'Jesse',
  'lastName': 'Tomson',
  'weight': '185'}]
'''

'''
Notice it alphabetized the keys within each dictionary (dob before firstName) — that's pprint's default sorting behavior, not something you controlled. If you want to preserve your original key order, add sort_dicts=False: pprint(people, sort_dicts=False).
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

