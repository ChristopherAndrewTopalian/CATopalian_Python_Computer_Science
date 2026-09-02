# os_path_dirname_listdir_realpath_write.py

import os

path = os.path.dirname(os.path.realpath(__file__))

theData = os.listdir(path)

print(theData)

with open('theFiles.txt', 'w') as ourFile:
    ourFile.write(str(theData))

input('Press Enter to Exit')

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

