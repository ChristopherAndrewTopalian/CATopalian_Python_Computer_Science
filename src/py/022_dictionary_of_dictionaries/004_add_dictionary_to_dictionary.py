# add_dictionary_to_dictionary.py

world = {}

first_name = input("Enter First name: ")
last_name = input("Enter Last name: ")

name_dictionary = {
    "First name": first_name,
    "Last name": last_name
}

world[first_name] = name_dictionary

print(world)

####

'''
Enter First name: Christopher
Enter Last name: Topalian
{'Christopher': {'First name': 'Christopher', 'Last name': 'Topalian'}}
'''

'''
{
    'Christopher':
    {
        'First name': 'Christopher',
        'Last name': 'Topalian'
    }
}
'''

####

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian

