from textual.app import ComposeResult
from textual.containers import Grid, Horizontal, Vertical
from textual.widgets import Static, OptionList, Checkbox, Input


from globals import *

class pwadLaunchOptions(Static):
    """Main Launch Options generator UI"""
    def compose(self) -> ComposeResult:
        yield Grid(
            Grid(
                Checkbox("[b]Skill Level:[/b]", id='skill-level-checkbox', 
                         classes='skillOptionElement'),
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
                        Checkbox("Fast   ", id="fast-monst", classes="misc-option-element"),
                        Checkbox("Respawn", id="respawn-monst", classes="misc-option-element"),
                        id="nightmare-opts-grid",
                    ),
                    Vertical(
                        # This is really bad, but I'm tired of fixing things
                        Checkbox("Auto Warp", id='auto-warp-checkbox', 
                                 classes="misc-option-element"),
                        Checkbox("No Cheats  ", id="no-cheats", classes="misc-option-element"), # Must have 11 spaces
                        Checkbox("No Monsters", id="no-monst", classes="misc-option-element"),
                        id="weird-opts-grid",
                    ),
                    id="flags-option-grid",
                ),
                id="miscGrid",
                classes="innerLaunchOptsGrid"
            ),
            id="pwadLaunchOptionsGrid"
        )
    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        # This is the most modular I could get
        LAUNCH_FLAGS[event.checkbox.id] = event.checkbox.value
            
