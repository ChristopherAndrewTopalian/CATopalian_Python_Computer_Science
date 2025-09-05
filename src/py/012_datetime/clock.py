# clock.py

import time
import datetime as dt

def makeUpdatingClock():
    while True:
        print(dt.datetime.now().strftime("%I:%M:%S %p"), end = "\r")

        time.sleep(1)

####

makeUpdatingClock()

####

'''
03:25:52
'''

####

# The \r makes the cursor return
# to the beginning of the line,
# so the time gets overwritten
# every second instead of
# printing a new line.

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

