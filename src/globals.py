from pathlib import Path
import sys
import os

# GLOBAL PARAMS
# Some of them are placeholders. TODO: Make configs and change the params
home = Path.home()

try: 
    os.chdir(sys._MEIPASS)
except (NameError, AttributeError) as error:
    print(f"{error}. Expected to be running as script, not frozen.")

JSON_FILEPATH = 'src/ml_info.json'
SELECTED_FILE = 'ATTACK.WAD'

# GLOBAL BOOLS
QUICK_EXIT = False
