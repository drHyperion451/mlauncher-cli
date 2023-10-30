from textual.app import ComposeResult
from textual.containers import Grid, HorizontalScroll, Horizontal, Vertical
from textual.screen import Screen
from textual.validation import Number, Function
from textual.widgets import Label, Button, Placeholder, Static, OptionList, \
Checkbox, Input

from globals import *
from i_jsonUtils import MapsJson


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
            Grid(
                Checkbox("[b]Skill Level:[/b]", id='skill-level-button', 
                         classes='launchOptionButton skillOptionElement'),
                OptionList(# id: skillList classes:skillOptionElement
                    "I'm too young to die",
                    "Hey, not too rough",
                    "Hurt me plenty",
                    "Ultra-Violence",
                    "Nightmare!",
                    id='skillList',
                    classes="skillOptionElement",
                    disabled=False,
                    wrap=False,
                ),
                id="skillLevelGrid",
                classes="innerLaunchOptsGrid"
            ),
            Grid(
                Horizontal(
                    Vertical(
                        Input(id="warp-input", placeholder="Warp Map", 
                              classes="misc-option-element"),
                        Checkbox("Fast   ", classes="misc-option-element"),
                        Checkbox("Respawn", classes="misc-option-element"),
                        id="nightmare-opts-grid",
                    ),
                    Vertical(
                        # This is really bad, but I'm tired of fixing things
                        Checkbox("Point to ML", id='auto-warp-checkbox', 
                                 classes="misc-option-element"),
                        Checkbox("No Cheats  ", classes="misc-option-element"), # Must have 11 spaces
                        Checkbox("No Monsters", classes="misc-option-element"),
                        id="weird-opts-grid",
                    ),
                    id="flags-option-grid",
                ),
                id="miscGrid",
                classes="innerLaunchOptsGrid"
            ),
            id="pwadLaunchOptionsGrid"
        )
