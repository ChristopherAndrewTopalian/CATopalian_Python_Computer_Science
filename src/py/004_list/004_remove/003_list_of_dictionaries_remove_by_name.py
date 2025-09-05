# list_of_dictionaries_remove_by_name.py

people = [
    {
        'name': 'Jane',
        'score': 95
    },
    {
        'name': 'Melissa',
        'score': 98
    },
    {
        'name': 'Tabitha',
        'score': 93
    }
]

for z in people:
    if z['name'] == 'Melissa':
        people.remove(z)
        break

print(len(people))

print(people)

input('Press Enter to Exit')

####

'''
2
[{'name': 'Jane', 'score': 95}, {'name': 'Tabitha', 'score': 93}]
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

