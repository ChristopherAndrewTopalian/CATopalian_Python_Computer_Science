# make_new_folder_format_string.py

import os
import getpass

username = getpass.getuser()

thePath = r"C:\Users\{}\Desktop\ourFolder".format(username)

if not os.path.exists(thePath):
    try:
        os.mkdir(thePath)
    except OSError as theError:
        print(f"Creation of the directory {thePath} failed: {theError}")
    else:
        print(f"Successfully created the directory {thePath}")
else:
    print(f"The directory {thePath} already exists.")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

