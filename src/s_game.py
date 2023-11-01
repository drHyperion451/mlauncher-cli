"""
'GAME' screen.
"""

from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Label, Input, Footer

from globals import GlobalVars, SETTINGS_PATH
from configparser import ConfigParser

class GameScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]
    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Game Options:", id='game-dialog-title'),
            Grid(
                Label('Source Port: '),
                Input(value=GlobalVars.SOURCEPORT, id='source-port-input'),
                Label('iWad selector: '),
                Input(value=GlobalVars.IWAD, id='iwad-input'),
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
            case 'source-port-input':
                GlobalVars.SOURCEPORT = event.input.value
                config.set('GAME', 'SOURCEPORT', str(event.input.value))
            case 'iwad-input':
                GlobalVars.IWAD = event.input.value
                config.set('GAME', 'IWAD', str(event.input.value))
        with open(SETTINGS_PATH, 'w') as configfile:
                    config.write(configfile)