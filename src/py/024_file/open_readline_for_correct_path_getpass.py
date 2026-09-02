# open_readline_for_correct_path_getpass.py

from pathlib import Path
import getpass

username = getpass.getuser()

file_path = Path('C:/') / 'Users' / username / 'Desktop' / 'testFile.txt'

with open(file_path, 'r') as theData:
    for line in theData:
        print(line, end='')

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

