# and.py

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox

def gate_and(a, b):
    if a == 1 and b == 1:
        return "Both True"
    else:
        return "Choose the correct combination of 0 and 1"

####

def display_it(label):
    result = gate_and(1, 1)  # simulate AND gate with (1, 1)
    label.setText(result)

    # show message box with the AND gate result
    QMessageBox.information(None, "AND Gate", result)

####

def start_app():
    # create the application
    app = QApplication(sys.argv)

    # create the main window
    window = QWidget()
    window.setWindowTitle("AND Gate")
    window.setGeometry(100, 100, 300, 200)

    # create layout and widgets
    layout = QVBoxLayout()
    
    label = QLabel("Press the button to see the AND gate result")
    layout.addWidget(label)

    button = QPushButton("Test AND Gate with (1, 1)")
    button.clicked.connect(lambda: display_it(label))
    layout.addWidget(button)

    # set layout to the window
    window.setLayout(layout)
    window.show()

    # execute the app
    sys.exit(app.exec())

####

if __name__ == "__main__":
    start_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2025
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

