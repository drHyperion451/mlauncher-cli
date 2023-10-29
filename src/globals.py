from pathlib import Path
import sys
import os
from configparser import ConfigParser

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



def SETTINGS_CREATE(settings_path):
    config = ConfigParser()
    """Manually add sections below"""
    config['GAME'] = SETTINGS_GAME # Set in the globals.py file

    with open(settings_path, 'w') as configfile:
        config.write(configfile)


SETTINGS_V = 1 # Whenever I change the config this should add to avoid problems
SETTINGS_PATH = 'config.ini'
""" Edit SETTINGS_CREATE inside ui_settings.py for adding more sections
    Each SETTINGS_* variable is one section"""

SETTINGS_GAME:dict = {'SOURCEPORT': './dsda-doom/dsda-doom.exe',
                'IWAD': './doom2/DOOM2.WAD',
                'ML_PATH': './master/wads',
                'SELECTED_MAP': 'ATTACK.WAD',
                'FILES': ''}


config = ConfigParser()
if not os.path.exists(SETTINGS_PATH):
        SETTINGS_CREATE(SETTINGS_PATH)
config.read(SETTINGS_PATH)
SOURCEPORT = config.get('GAME', 'SOURCEPORT')
IWAD = config.get('GAME', 'IWAD')
ML_PATH = config.get('GAME', 'ML_PATH')
FILES = config.get('GAME', 'FILES')
SELECTED_MAP = config.get('GAME', 'SELECTED_MAP')
        
# GLOBAL BOOLS
QUICK_EXIT = False
