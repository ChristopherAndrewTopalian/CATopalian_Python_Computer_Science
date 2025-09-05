# date_time_ctime_24.py

import time

# get current time in seconds since epoch
theSeconds = time.time()

# format seconds into a readable date time
theDateTime = time.ctime(theSeconds)

print(theDateTime)

input('Press Enter to Exit')

####

'''
Fri Oct 18 03:40:29 2024
'''

####

# time.time() returns the number
# of seconds that have passed
# since the Unix epoch (January 1, 1970)

# time.ctime(theSeconds) converts
# seconds into a human readable string,
# with a 24 hour format

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

