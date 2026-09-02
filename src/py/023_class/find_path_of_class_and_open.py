# find_path_of_class_and_open.py

import datetime
import inspect
import os

# Get the file path of the datetime module
datetime_path = inspect.getfile(datetime)
print(f"Path of datetime module: {datetime_path}")

# Check if the path is a file and readable
if os.path.isfile(datetime_path):
    with open(datetime_path, 'r') as file:
        content = file.read()
        print("Content of the datetime module:")
        print(content)
else:
    print("The datetime module is a built-in module and does not have a .py file.")

input('Press Enter to Exit')

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian

