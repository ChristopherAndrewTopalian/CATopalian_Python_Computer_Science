:: CATopalian_Combine_PY_Format_for_MD.bat

@echo off
:: set the output file name
set "output=main.md"

:: set language (python, javascript, etc.)
set "language=python"

:: clear existing output file
type nul > "%output%"

:: loop through all py files in subdirectories
for /r %%i in (*.py) do (

    :: append the opening code block for the specified language
    echo ```%language% >> "%output%"
    
    :: append the content of each file to the output file
    type "%%i" >> "%output%"
    
    :: append the closing code block
    echo ``` >> "%output%"
)

echo "Files combined into %output% successfully."

:: For bigger projects with many PY files, the process will take a few moments longer, as we witness the main.md file size getting bigger as it builds the file!
:: We make sure to let the process complete, so that all PY content is copied and formatted completely.

:: IMPORTANT: Make sure there is a NEW LINE at the end of each of the PY scripts in our folder!
:: This ensures proper formatting in our generated main.md file.

:: Dedicated to God the Father
:: (c) Copyright 2000-2026 Christopher Andrew Topalian. All Rights Reserved.
:: https://github.com/ChristopherAndrewTopalian

