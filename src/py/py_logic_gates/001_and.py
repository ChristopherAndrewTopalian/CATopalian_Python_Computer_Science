# py_logic_gate_001_and.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 1

if (A == 1 and B == 1):
    print('Both True')

    windll.user32.MessageBoxW(0,
    'Both True', 'AND Gate', 0)

input('Press Enter to Exit')

####

# AND GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  0
# 1  0  =  0
# 1  1  =  1

# AND 0001

# Activates Only if Both True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

