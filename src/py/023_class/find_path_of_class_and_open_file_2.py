# find_path_of_class_and_open_file_2.py

import datetime
import inspect
import os
import subprocess
import platform

def open_module_in_editor(module):
    try:
        # Get the file path of the module
        module_path = inspect.getfile(module)
        print(f"Path of the module: {module_path}")

        # Check if the path is a file and readable
        if os.path.isfile(module_path):
            editor = "code"  # Replace with your preferred editor's command
            # Open the file in the specified editor based on the operating system
            if platform.system() == 'Windows':
                f = open(module_path, "r")
                print(f.read()) 
                #subprocess.call([editor, module_path])
            elif platform.system() == 'Darwin':  # macOS
                subprocess.call([editor, module_path])
            else:  # Linux and other Unix-like systems
                subprocess.call([editor, module_path])
        else:
            print(f"{module.__name__} is a built-in module and does not have a .py file.")
    except TypeError:
        print(f"{module.__name__} is a built-in module and does not have a .py file.")

# Example usage
open_module_in_editor(datetime)

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian

