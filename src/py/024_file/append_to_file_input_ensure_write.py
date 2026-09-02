import os

with open('text001.txt', 'a') as file:
    while True:
        words = input('Enter words (or "exit"): ')
        if words.lower() == 'exit': break
        
        file.write(words + '\n')
        
        # Force the data out of Python's buffer
        file.flush()
        # Force the OS to write to the physical disk
        os.fsync(file.fileno())

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

