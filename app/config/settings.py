"""
You can create a file in this same directory called local.py to create
local overrides for the settings found below.
"""

import os

EMAIL = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

try:
    from .local import *
    print("USING LOCAL SETTINGS OVERRIDES")
except Exception:
    print("USING REGULAR SETTINGS")
