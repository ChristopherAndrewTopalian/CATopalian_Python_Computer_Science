# make_folder_if_not_already_made.py

import os

folderName = "ourNewFolder"

# check if folder exists
if not os.path.exists(folderName):
    # create new folder
    os.makedirs(folderName)
    print(f"Folder '{folderName}' created.")
else:
    print(f"Folder '{folderName}' already exists.")

####

'''
Makes a new folder with a specified name if it doesn't already exist.
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

