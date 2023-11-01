from pathlib import Path
import sys
from pathlib import Path
from configparser import ConfigParser
from i_jsonUtils import MapsJson
# GLOBAL PARAMS
home = Path.home()
JSON_FILEPATH = 'src/ml_info.json'
SETTINGS_PATH = 'config.ini'
if getattr(sys, 'frozen', True):
    JSON_FILEPATH = Path(sys._MEIPASS) / "src" / "ml_info.json"
    SETTINGS_PATH = f"{Path(sys._MEIPASS).parent}/config.ini"
maps = MapsJson(JSON_FILEPATH)
try: 
    """
    This is needed if you want to freeze the script. If not, it won't load
    correctly. 
    """
    JSON_FILEPATH = Path(sys._MEIPASS) / "src" / "ml_info.json"
    SETTINGS_PATH = f"{Path(sys._MEIPASS).parent}/config.ini"
except (NameError, AttributeError) as error:
    print(f"{error}. Expected to be running as script, not frozen.")




def SETTINGS_CREATE(settings_path):
    config = ConfigParser()
    config.read(settings_path)

    # Define the sections and their corresponding dictionaries
    sections = {
        'GAME': SETTINGS_GAME,
        'LAUNCHER': SETTINGS_LAUNCHER
    }

    # Iterate through the sections and their dictionaries
    for section, settings_dict in sections.items():
        # If the section is missing, add it
        if not config.has_section(section):
            config.add_section(section)

        # Iterate through the keys and values in the dictionary
        for key, value in settings_dict.items():
            # If the key is missing, add it
            if not config.has_option(section, key):
                config.set(section, key, str(value))

    # Write the updated configuration to the file
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
    'FILES': '',
    'SKILL': 4,
}

SETTINGS_LAUNCHER:dict = {
    'SETTINGS_V': SETTINGS_V,
    'QUICK_EXIT': 'False',
    'WADS_ORDER': 'PSN'
}


config = ConfigParser()
#if not os.path.exists(SETTINGS_PATH):
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
class GlobalVars:
# For persistence when saving the game
    SOURCEPORT = config.get('GAME', 'SOURCEPORT')
    IWAD = config.get('GAME', 'IWAD')
    ML_PATH = config.get('GAME', 'ML_PATH')
    FILES = config.get('GAME', 'FILES')
    SELECTED_MAP = config.get('GAME', 'SELECTED_MAP')
    SKILL = config.get('GAME', 'SKILL')
    WARP = str('')
# WARP_PC is the PC slot from the SELECTED_MAP for auto-warping
    WARP_PC = maps.get_from_data('WAD', SELECTED_MAP, 'PC')[0] 
# GLOBAL BOOLS
    QUICK_EXIT = config.get('LAUNCHER', 'QUICK_EXIT')
    WADS_ORDER = config.get('LAUNCHER', 'WADS_ORDER')

# Flags
    LAUNCH_FLAGS_STATUS = {
        'skill-level-checkbox' : False,
        'skill-level': False,
        'fast-monst' : False,
        'respawn-monst' : False,
        'warp-level': False,
        'auto-warp-checkbox' : False,
        'no-cheats' : False,
        'no-monst' : False,
    }
    LAUNCH_FLAGS = {
        'skill-level-checkbox' : None,
        'skill-level': '-skill',
        'fast-monst' : '-fast',
        'respawn-monst' : '-respawn',
        'warp-level': '-warp',
        'auto-warp-checkbox' : None,
        'no-cheats' : '-nocheats',
        'no-monst' : '-nomonsters',
    }
SKILL_OPTIONS = ("I'm too young to die", "Hey, not too rough", 
                 "Hurt me plenty", "Ultra-Violence", "Nightmare!")
# STDOUT, STDERR
O_STDOUT = ''
O_STDERR = ''
