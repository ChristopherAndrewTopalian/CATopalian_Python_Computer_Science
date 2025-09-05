:: zShowCode.bat

@echo off

set "pyFile="

for %%f in (*.py) do set "pyFile=%%f" & goto :open_editor

:open_editor
if defined pyFile (
    echo Opening the file in the default editor: %pyFile%
    start "" "%pyFile%"
) else (
    echo No Python files found in the directory.
)

pause

:: Dedicated to God the Father
:: All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
:: https://github.com/ChristopherTopalian
:: https://github.com/ChristopherAndrewTopalian
:: This .bat File shows the code of a .py file in the folder.
:: To activate this .bat file, we double click the .bat file, while it is located in our  folder.