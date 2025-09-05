# list_image_file_names_all_folders_list.py

import os

currentFolder = os.getcwd()

imageFiles = []

for dirpath, dirnames, filenames in os.walk(currentFolder):
    for file in filenames:
        if file.endswith(('.jpg', '.png', '.jpeg', 'gif')):
            imageFiles.append(file)

####

print(imageFiles)

input('Press Enter to Exit')

####

'''
['001.jpg', '002.jpg', '007.jpg', '007.png', 'tree.gif']
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

