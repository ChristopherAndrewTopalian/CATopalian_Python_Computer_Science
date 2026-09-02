# pathlib_path_iterdir_append_fileNames.py

import pathlib

flist = [ ]

for thePath in pathlib.Path('.').iterdir():
    if thePath.is_file():
        print(thePath)
        flist.append(thePath)

input("Press Enter to Exit")

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

