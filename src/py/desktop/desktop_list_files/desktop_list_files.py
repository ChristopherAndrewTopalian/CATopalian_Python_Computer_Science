# desktop_list_files.py

import os
import getpass

# get current username
username = getpass.getuser()

thePath = "C:\\Users\\" + username + "\\Desktop"

print(thePath)

files = os.listdir(thePath)

print(files)

####

'''
for f in files:
    print(f)
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

