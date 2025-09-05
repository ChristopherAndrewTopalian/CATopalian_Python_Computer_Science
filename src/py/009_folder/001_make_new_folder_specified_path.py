# make_new_folder_specified_path.py

import os

# rename OurUsername to your username
thePath = r"C:\Users\OurUsername\Desktop\ourFolder"

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

