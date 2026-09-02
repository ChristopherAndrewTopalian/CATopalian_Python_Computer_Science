# find_path_of_class_and_open_file.py

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
            # Open the file in the default editor based on the operating system
            if platform.system() == 'Windows':
                os.startfile(module_path)
            elif platform.system() == 'Darwin':  # macOS
                subprocess.call(('open', module_path))
            else:  # Linux and other Unix-like systems
                subprocess.call(('xdg-open', module_path))
        else:
            print(f"{module.__name__} is a built-in module and does not have a .py file.")
    except TypeError:
        print(f"{module.__name__} is a built-in module and does not have a .py file.")

# Example usage
open_module_in_editor(datetime)

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian

