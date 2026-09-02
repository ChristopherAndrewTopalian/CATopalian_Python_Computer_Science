# dictionary_of_dictionaries_sort_by_key.py

pokemon = {
    "pikachu": {
        "name": "Pikachu",
        "type": "Electric",
        "friend": "Ash"
    },

    "charizard": {
        "name": "Charizard",
        "type": "Fire",
    },

    "charmander": {
        "name": "Charmander",
        "type": "Fire",
    }
}

# Sort by the inner 'name' key
sorted_pokemon = dict(sorted(
    pokemon.items(),
    key=lambda item: item[1]['name']
))

print(sorted_pokemon)

'''
# Print the sorted dictionary
for key, data in sorted_pokemon.items():
    print(key, data)
'''

'''
{'charizard': {'name': 'Charizard', 'type': 'Fire'}, 'charmander': {'name': 'Charmander', 'type': 'Fire'}, 'pikachu': {'name': 'Pikachu', 'type': 'Electric', 'friend': 'Ash'}}
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

