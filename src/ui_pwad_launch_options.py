from textual.app import ComposeResult
from textual.containers import Grid, Horizontal, Vertical
from textual.widgets import Static, OptionList, Checkbox, Input


from globals import SKILL_OPTIONS, GlobalVars

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
                    disabled=True,
                    wrap=False,
                ),
                id="skillLevelGrid",
                classes="innerLaunchOptsGrid"
            ),
            Grid(
                Horizontal(
                    Vertical(
                        Input(id="warp-input", placeholder="Warp Map", 
                              classes="misc-option-element", disabled=False),
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
        GlobalVars.LAUNCH_FLAGS_STATUS[event.checkbox.id] = event.checkbox.value
        if event.checkbox.id == 'skill-level-checkbox':
            # This enables the skilllist when the checkbox is enabled
            self.query_one('#skillList').disabled = not event.checkbox.value
            # TODO: Change selector to the SKILL defined previously in config.ini
        if event.checkbox.id == 'auto-warp-checkbox':
            # Disables warp input if auto warp is enabled.
            # THIS DOESN'T WORK?? Maybe it's a Textual Bug?? TODO: Open a ticket
            self.query_one('#warp-input').disabled == event.checkbox.value
    
    def on_option_list_option_highlighted(self, event: OptionList.OptionHighlighted) -> None:
        # Works when skill level is enabled
        if self.query_one('#skill-level-checkbox').value == True:
            GlobalVars.SKILL = SKILL_OPTIONS.index(event.option.prompt) + 1
    
    def on_input_changed(self, event: Input.Submitted) -> None:
        if self.query_one('#auto-warp-checkbox').value == False:
            GlobalVars.WARP = event.value



            
            
