# get_file_path.py

import pathlib

def getThisScriptFilePath():
    fileName = pathlib.Path(__file__).parent.resolve()

    return fileName

print(__file__)

input('Press Enter to Exit')

# returns for example:
# D:\_1Code\_2PY\_0\Topalian_Python_Date\py\path

# It does not include the file name itself, which in this case is getFilePath.py

# The special variable __file__ contains the path to the current file.
# From that we can get the directory using pathlib
# or we could alternatively use os.path module.

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian

