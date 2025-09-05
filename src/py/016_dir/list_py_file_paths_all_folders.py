# list_py_file_paths_all_folders.py

import os

currentFolder = os.getcwd()

for dirpath, dirnames, filenames in os.walk(currentFolder):
    for file in filenames:
        if file.endswith('.py'):
            print(os.path.join(dirpath, file))

####

input('Press Enter to Exit')

####

# D:\ourFolder\py\dir\listdir.py

#D:\ourFolder\py\dir\list_py_file_paths_all_folders.py

#D:\ourFolder\py\dir\listdir_endswith.py

#D:\ourFolder\py\dir\New folder\test.py

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

