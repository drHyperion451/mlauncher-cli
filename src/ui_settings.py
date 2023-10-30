from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Label, Button, Placeholder, Static

from globals import *



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

class pwadLaunchOptions(Static):
    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Difficulty", id='difficultyLabel', classes='launchOptionsLabel'),
            id="pwadLaunchOptionsGrid"
        )