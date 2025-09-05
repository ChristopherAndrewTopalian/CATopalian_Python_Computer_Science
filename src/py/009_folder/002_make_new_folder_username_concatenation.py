# make_new_folder_username_concatenation.py

import os
import getpass

# get current username
username = getpass.getuser()

thePath = "C:\\Users\\" + username + "\\Desktop\\ourFolder"

if not os.path.exists(thePath):
    try:
        os.mkdir(thePath)
    except OSError as theError:
        print("Creation of the directory " + thePath + " failed: " + str(theError))
    else:
        print("Successfully created the directory " + thePath)
else:
    print("The directory " + thePath + " already exists.")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

