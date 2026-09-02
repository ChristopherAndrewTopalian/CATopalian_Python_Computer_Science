# open_readline_for_correct.py

import os

file_path = os.path.join('C:' + os.sep, 'Users', 'ourUserName', 'Desktop', 'testFile.txt')

with open(file_path, 'r') as theData:
    for line in theData:
        print(line, end='')

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

