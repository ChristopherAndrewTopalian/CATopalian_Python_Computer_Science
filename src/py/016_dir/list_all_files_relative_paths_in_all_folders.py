# list_all_files_relative_paths_in_all_folders.py

import os

# get current working directory
currentFolder = os.getcwd()

# walk through all folders and subfolders
for dirpath, dirnames, filenames in os.walk(currentFolder):
    # check each file in current folder
    for file in filenames:
        # get full path
        fullPath = os.path.join(dirpath, file)
        
        # get relative path from currentFolder
        relativePath = os.path.relpath(fullPath, currentFolder)
        
        print(relativePath)

####

input('Press Enter to Exit')

####

# image_gallery.html
# listdir.py
# listdir_endswith.py
# list_all_files_in_all_folders.py
# list_all_files_relative_paths_in_all_folders.py
# list_all_file_paths_in_all_folders.py
# list_image_file_names_all_folders_list.py
# list_py_file_names_all_folders.py
# list_py_file_names_all_folders_list.py
# list_py_file_paths_all_folders.py
# make_folder_if_not_already_made.py
# notes.txt
# New folder\001.jpg
# New folder\002.jpg
# New folder\008.jpg
# New folder\008.png

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

