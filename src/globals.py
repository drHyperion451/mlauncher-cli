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
    try:
        JSON_FILEPATH = Path(sys._MEIPASS) / "src" / "ml_info.json"
        SETTINGS_PATH = f"{Path(sys._MEIPASS).parent}/config.ini"
    except AttributeError as error:
        print(f"{error}. Expected to be running as script, not frozen.")

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
    O_STDOUT = 'Nothing here to show!'
    O_STDERR = 'It will appear errors here:'
    O_STDERR = """\
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi lobortis turpis vitae pretium lacinia. In sit amet tellus auctor, luctus mi sit amet, auctor risus. In semper augue at ornare tincidunt. Aliquam dictum ultricies erat, quis feugiat nisl molestie non. Integer sed ipsum sit amet dolor rhoncus pulvinar. In maximus pulvinar tincidunt. Donec vulputate vel tellus et laoreet.

In a turpis vestibulum erat semper cursus nec a augue. Quisque id rutrum felis. Pellentesque molestie ligula et justo tempor, ut vestibulum neque porttitor. Maecenas mattis nisi vitae facilisis rutrum. Nullam eget quam eu lacus rutrum bibendum nec a sapien. Proin vestibulum posuere turpis vel tempus. Aenean eget tristique justo. Mauris vel tincidunt turpis. Mauris suscipit vel eros eu pretium. Integer at metus non metus tincidunt rutrum. Etiam vel elit vel arcu faucibus auctor et at est. Suspendisse vel egestas tortor, at varius enim. Sed egestas hendrerit lacus, sit amet vestibulum lorem sollicitudin malesuada. Vivamus consequat vehicula ornare. Morbi tincidunt tellus vel lobortis porta. Fusce sit amet quam vitae metus mollis bibendum.

Aliquam vel sem eu tellus porta molestie eget at mi. Duis pulvinar in sapien ac posuere. Nunc luctus diam id justo congue, in suscipit ligula porttitor. Integer lacus felis, euismod non leo at, sagittis auctor tellus. Etiam tristique, nisl at iaculis volutpat, lacus ante fermentum elit, dapibus aliquam ipsum eros tincidunt velit. Phasellus congue elit sed turpis sodales vehicula. Quisque volutpat sollicitudin lorem, ac auctor leo scelerisque ac.

Mauris egestas, dui in vehicula laoreet, nunc enim laoreet dui, at laoreet purus massa id lectus. Aliquam leo dolor, auctor porttitor dignissim sit amet, ornare sit amet erat. Nullam imperdiet arcu ac justo dapibus condimentum. Etiam egestas hendrerit dui, a fringilla nisl. Cras sagittis odio vitae turpis hendrerit, eget dapibus nulla dapibus. Curabitur in posuere velit, ac faucibus est. Aliquam erat volutpat. Vestibulum velit velit, auctor fermentum volutpat at, feugiat a erat. Fusce quis elementum est.

In at dui vestibulum, commodo nibh ac, elementum elit. Sed scelerisque risus sit amet ante posuere dapibus. Nulla vel libero quis ex iaculis vestibulum a eu metus. Quisque mollis tellus metus, ut placerat justo semper placerat. Aenean quis cursus nulla. In hac habitasse platea dictumst. Sed bibendum condimentum tellus in vehicula. Nunc at orci eget sapien faucibus convallis id ut nibh. Cras nec elit dolor. Praesent cursus magna id justo tincidunt accumsan. Nam tincidunt lorem dui, a iaculis magna auctor nec. Sed porttitor sit amet leo eu condimentum. 
"""

SKILL_OPTIONS = ("I'm too young to die", "Hey, not too rough", 
                 "Hurt me plenty", "Ultra-Violence", "Nightmare!")
# STDOUT, STDERR

