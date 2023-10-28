from pathlib import Path
import sys
import os

# GLOBAL PARAMS
# Some of them are placeholders. TODO: Make configs and change the params
home = Path.home()

JSON_FILEPATH = 'src/ml_info.json'
try: 
    """
    This is needed if you want to freeze the script. If not, it won't load
    correctly. 
    """
    JSON_FILEPATH = f"{sys._MEIPASS}/src/ml_info.json"
except (NameError, AttributeError) as error:
    print(f"{error}. Expected to be running as script, not frozen.")


SELECTED_FILE = 'ATTACK.WAD'

# GLOBAL BOOLS
QUICK_EXIT = False
