from pathlib import Path

file_path = Path('C:/') / 'Users' / 'ourUserName' / 'Desktop' / 'testFile.txt'

with open(file_path, 'r') as theData:
    for line in theData:
        print(line, end='')

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

