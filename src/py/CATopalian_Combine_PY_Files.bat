:: CATopalian_Combine_PY_Files.bat

@echo off
:: set the output file name
set "output=main.pyw"

:: clear existing output file
type nul > "%output%"

:: loop through all Python files in subdirectories
for /r %%i in (*.py) do (
    :: append the content of each file to the output file
    type "%%i" >> "%output%"
)

echo "Python files combined into %output% successfully."

:: Dedicated to God the Father
:: (c) Copyright 2000-2026 Christopher Andrew Topalian. All Rights Reserved.
:: https://github.com/ChristopherAndrewTopalian

:: This .bat File Combines All .py files in all folders of our folder, into one main.py file.

:: To activate this .bat file, we double click the .bat file, while it is located in our py folder.