from pathlib import Path
import sys
import os
from pathlib import Path
from configparser import ConfigParser

# GLOBAL PARAMS
home = Path.home()

JSON_FILEPATH = 'src/ml_info.json'
SETTINGS_PATH = 'config.ini'
try: 
    """
    This is needed if you want to freeze the script. If not, it won't load
    correctly. 
    """
    JSON_FILEPATH = f"{sys._MEIPASS}/src/ml_info.json"
    SETTINGS_PATH = f"{Path(sys._MEIPASS).parent}/config.ini"
except (NameError, AttributeError) as error:
    print(f"{error}. Expected to be running as script, not frozen.")



def SETTINGS_CREATE(settings_path):
    config = ConfigParser()
    """Manually add sections below"""
    config['GAME'] = SETTINGS_GAME 
    config['LAUNCHER'] = SETTINGS_LAUNCHER

    with open(settings_path, 'w') as configfile:
        config.write(configfile)


SETTINGS_V:int = 1 # Whenever I change the config this should add to avoid problems

""" Edit SETTINGS_CREATE inside ui_settings.py for adding more sections
    Each SETTINGS_* variable is one section"""

SETTINGS_GAME:dict = {
    'SOURCEPORT': './dsda-doom/dsda-doom.exe',
    'IWAD': './doom2/DOOM2.WAD',
    'ML_PATH': './master/wads',
    'SELECTED_MAP': 'ATTACK.WAD',
    'FILES': ''
}

SETTINGS_LAUNCHER:dict = {
    'SETTINGS_V': SETTINGS_V,
    'QUICK_EXIT': 'False',
    'WADS_ORDER': 'PSN'
}


config = ConfigParser()
if not os.path.exists(SETTINGS_PATH):
    SETTINGS_CREATE(SETTINGS_PATH)
config.read(SETTINGS_PATH)
# If settings version are not the same, display an error message
SETTINGS_V_FILE:int = int(config.get('LAUNCHER', 'SETTINGS_V'))
if SETTINGS_V != SETTINGS_V_FILE: 
    # TODO: Fix this crap.
    print(
f"""ERROR: The version of the config file ({SETTINGS_V_FILE}) is not
the same as the current supported version ({SETTINGS_V}).

That means the app has created additional configs that won't work on the new
update, so you need to manually add them

Please backup the config.ini file, delete it and change the new info.
This shitty workaround is planned to be reworked for avoiding user 
headaches. Sorry! :(

If you think you know what you are doing you can replace the settings_v to match
the current one {SETTINGS_V}."""
)
    input('Press any button to exit')
    exit()

SOURCEPORT = config.get('GAME', 'SOURCEPORT')
IWAD = config.get('GAME', 'IWAD')
ML_PATH = config.get('GAME', 'ML_PATH')
FILES = config.get('GAME', 'FILES')
SELECTED_MAP = config.get('GAME', 'SELECTED_MAP')
        
# GLOBAL BOOLS
QUICK_EXIT = config.get('LAUNCHER', 'QUICK_EXIT')
WADS_ORDER = config.get('LAUNCHER', 'WADS_ORDER')
