from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Label, Button, Placeholder

from configparser import ConfigParser
import os

    
class Settings():
    """Creates config.ini if not created. Dictates which stuff should be inside
    it, and reads it."""
    def __init__(self, settings_path='config.ini') -> None:
        self.config = ConfigParser()
        if not os.path.exists(settings_path):
            self.config['GAME'] = {'SOURCEPORT': './dsda-doom/dsda-doom.exe',
                            'IWAD': './doom2/DOOM2.WAD',
                            'ML_PATH': './master/wads'}
            
            with open(settings_path, 'w') as configfile:
                self.config.write(configfile)
        self.config.read(settings_path)
    def getOption(self, section, option):
        return self.config.get(section, option)



class SettingsScreen(Screen):
    """ An options screen class defined in ui_settings.py
    """
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]
    classes = 'dialogScreen'
    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Options", id='optionsTitle', classes='popupDialogTitle'),
            Button("Cancel", 'default', id="optionsCancel", classes='popupButton'),
            id="optionsDialog",
            classes='dialogGrid'
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case 'optionsCancel':
                self.app.pop_screen()

