# list_of_dictionaries_show_all_json.py

import json

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

print(json.dumps(people, indent=4))

input("Press Enter to Exit")

'''
[
    {
        "firstName": "John",
        "lastName": "Rambo",
        "dob": "3-1-1977",
        "weight": "170"
    },
    {
        "firstName": "Jesse",
        "lastName": "Tomson",
        "dob": "1-8-1978",
        "weight": "185"
    }
]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

