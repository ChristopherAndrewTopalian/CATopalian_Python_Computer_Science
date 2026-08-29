# dictionary_of_dictionaries_lookup.py

fleet = {
    "rover_01": {
        "type": "Scout",
        "speed": 15.5,
        "weapons": ["LiDAR", "Ultrasonic"],
    },
    "tank_01": {
        "type": "Heavy",
        "speed": 6.0,
        "weapons": ["120mm", "Smoke"],
    },
}

# INSTANT LOOKUP
print(fleet["rover_01"]["speed"])  # Output: 15.5

# DYNAMIC LOOKUP BY VARIABLE
active_id = "tank_01"
print(fleet[active_id]["weapons"][1])  # Output: Heavy

####

# Dedicated to God the Father
# (c) Copyright 2000-2026 Christopher Andrew Topalian. All rights reserved.
# https://github.com/ChristopherAndrewTopalian

