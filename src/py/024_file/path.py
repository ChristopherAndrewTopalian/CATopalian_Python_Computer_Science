# path.py

import os

def get_file_path(file_name):
    # Get the absolute path of the file
    absolute_path = os.path.abspath(file_name)
    return absolute_path

# Example usage
file_name = 'example_file.py'

file_path = get_file_path(file_name)

print(f"The absolute path of the file is: {file_path}")

input('Press Enter to Exit')

"""
    Get the absolute path of a file.
    
    Parameters:
    file_name (str): The name or relative path of the file.
    
    Returns:
    str: The absolute path of the file.
"""

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

