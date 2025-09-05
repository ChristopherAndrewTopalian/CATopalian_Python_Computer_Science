# py_logic_gate_006_xnor.py

from ctypes import*

windll.shcore.SetProcessDpiAwareness(1)

A = 1
B = 1

if ((A == 0 and B == 0) or
    (A == 1 and B == 1)):
    print('Both True or Both False')

    windll.user32.MessageBoxW(0,
    'Both True or Both False', 'XNOR Gate', 0)

input('Press Enter to Exit')

####

# XNOR GATE Truth Table
# A  B
# 0  0  =  1
# 0  1  =  0
# 1  0  =  0
# 1  1  =  1

# XNOR 1001

# Activates Only if Both True
# or Both False

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

