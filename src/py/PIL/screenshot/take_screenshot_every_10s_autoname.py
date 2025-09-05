# take_screenshot_every_10s_autoname.py

from PIL import ImageGrab
import time
from datetime import datetime

# start loop to take screenshot every 10 seconds
while True:
    # get current time for filename
    now = datetime.now()
    # e.g., 2025-06-09_13-45-12
    timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')

    # capture the screen
    ourImage = ImageGrab.grab()

    # define filename
    filename = 'screenshot_' + timestamp + '.png'

    # save screenshot
    ourImage.save(filename)

    print('Saved:', filename)

    # wait 10 seconds
    time.sleep(10)

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

