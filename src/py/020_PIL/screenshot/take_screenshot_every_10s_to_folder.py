# take_screenshot_every_10s_to_folder.py

from PIL import ImageGrab
import time
import os
from datetime import datetime

# define folder name
folderName = 'screenshots'

# create the folder if it doesn't exist
if not os.path.exists(folderName):
    # create the folder
    os.makedirs(folderName)
    print('Created folder: ' + folderName)

####

# start infinite screenshot loop
while True:
    # generate timestamp for filename
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')

    # build full file path
    filename = folderName + '/screenshot_' + timestamp + '.png'

    # take screenshot
    ourImage = ImageGrab.grab()

    # save image
    ourImage.save(filename)

    print('Saved:', filename)

    # wait 10 seconds before next screenshot
    time.sleep(10)

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

