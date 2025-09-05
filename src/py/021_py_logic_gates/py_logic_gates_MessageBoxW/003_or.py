# py_logic_gate_003_or.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 0

if (A == 1 or B == 1):
    print('One or Both True')

    windll.user32.MessageBoxW(0,
    'One or Both True', 'OR Gate', 0)

input('Press Enter to Exit')

####

# OR GATE Truth Table
# A  B
# 0  0  =  0
# 0  1  =  1
# 1  0  =  1
# 1  1  =  1

# OR 0111

# Activates Only if One or Both True

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

