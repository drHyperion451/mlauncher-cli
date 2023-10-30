from textual.app import ComposeResult
from textual.containers import Grid, Horizontal, Vertical
from textual.widgets import Static, OptionList, Checkbox, Input

from globals import *

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
                        Checkbox("Auto Warp", id='auto-warp-checkbox', 
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
