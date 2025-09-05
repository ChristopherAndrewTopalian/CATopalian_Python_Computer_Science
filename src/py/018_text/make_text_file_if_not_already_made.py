# make_text_file_if_not_already_made.py

import os

fileName = "ourNewFile.txt"

# check if file exists
if not os.path.exists(fileName):
    # create new file
    with open(fileName, 'w') as file:
        file.write("This is a new text file.\n")
    print(f"File '{fileName}' created.")
else:
    print(f"File '{fileName}' already exists.")

####

'''
Makes a new text file with a specified name if it doesn't already exist.
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

