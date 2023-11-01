"""
'WADS' screen.
"""

from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Label, Button, Placeholder, Input, Footer

from globals import GlobalVars, SETTINGS_PATH
from configparser import ConfigParser

class WadsScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]
    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Master Levels Wads Options:", id='game-dialog-title'),
            Grid(
                Label('ML Wads folder: '),
                Input(value=GlobalVars.ML_PATH, id='wad-folder-input'),
                Label('Wads order: '),
                Input(value=GlobalVars.WADS_ORDER, placeholder="(A-Z), (Z-A), (PSN)", 
                      id='order-input'), # TODO: Dropdown Menu
                id='game-dialog-options',
                classes='dialog-options'
            ),
            Label("Paste the path here. You can edit them on the \
config.ini file too."),
            id='game-dialog',
            classes='dialogGrid'
        ) 
        yield Footer()
    def on_input_submitted(self, event: Input.Submitted) -> None:
        config = ConfigParser()
        config.read(filenames= SETTINGS_PATH)
        match event.input.id:
            case 'wad-folder-input':
                GlobalVars.ML_PATH = event.input.value
                config.set('GAME', 'ML_PATH', str(event.input.value))
            case 'order-input':
                GlobalVars.WADS_ORDER = event.input.value
                config.set('LAUNCHER', 'WADS_ORDER', str(event.input.value))
        with open(SETTINGS_PATH, 'w') as configfile:
                    config.write(configfile)