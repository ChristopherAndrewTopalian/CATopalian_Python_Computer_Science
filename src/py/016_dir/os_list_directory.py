# os_list_directory.py

import os

files = os.listdir('.')
print(files)

with open('check.txt', 'w') as ourFile:
    ourFile.write(str(files))

input("Press Enter to Exit")

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

