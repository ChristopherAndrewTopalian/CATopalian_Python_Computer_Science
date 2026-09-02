# class_Pokemon.py

class Pokemon:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def showInfo(self):
        print("Name: " + self.name + "\n" + "Kind: " + self.kind)

    # This controls how the object looks when printed inside a dictionary or list
    def __repr__(self):
        return f"{self.name} ({self.kind} type)"

pikachu = Pokemon(
    "Pikachu",   #name
    "Electric"   #kind
)

ash_inventory = {}

# Add Pikachu using his name as the dictionary key
ash_inventory[pikachu.name] = pikachu

print("Ash's Inventory")
print(ash_inventory)

# You can now retrieve Pikachu out of the dictionary by name to call his methods
print("\nPulling from Inventory")
ash_inventory['Pikachu'].showInfo()

input("\nPress Enter to Exit")

'''
Name: Pikachu
Kind: Electric
Press Enter to Exit
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

