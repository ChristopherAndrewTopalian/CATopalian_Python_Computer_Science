# list_py_file_names_all_folders_list.py

import os

currentFolder = os.getcwd()

pythonFiles = []

for dirpath, dirnames, filenames in os.walk(currentFolder):
    for file in filenames:
        if file.endswith('.py'):
            pythonFiles.append(file)

####

print(pythonFiles)

input('Press Enter to Exit')

####

'''
['listdir.py', 'listdir_endswith.py', 'list_py_file_names_all_folders.py', 'list_py_file_names_all_folders_list.py', 'list_py_file_paths_all_folders.py', 'test.py', 'notes.py']
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

