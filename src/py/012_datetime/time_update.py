# time_update.py

import time
from datetime import datetime as dt

def show_clock():
    while True:
        current_time = dt.now().strftime("%H:%M:%S")
        print(f"\r{current_time}", end="", flush=True)
        #print(current_time)
        time.sleep(1)

show_clock()

####

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian

