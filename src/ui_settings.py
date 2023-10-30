from textual.app import ComposeResult
from textual.containers import Grid, HorizontalScroll, Horizontal, Vertical
from textual.screen import Screen
from textual.validation import Number, Function
from textual.widgets import Label, Button, Placeholder, Static, OptionList, \
Checkbox, Input

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
