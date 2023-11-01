from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Label, Button

from time import time

class QuitScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]
    def compose(self) -> ComposeResult:
        yield Grid(
            Label(QuitMsg(), id="question", classes='popupDialogText'),
            Button("Quit", variant='error', id="buttonQuit", classes='popupButton'),
            Button("Cancel", variant='primary', id='buttonCancel', classes='popupButton'),
            id='closeDialog',
            classes='dialogGrid'
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'buttonQuit':
            self.app.exit()
        else:
            self.app.pop_screen()
    

# Misc Functions
def QuitMsg() -> str:
    """Funny Doom II tribute.

    Returns:
        str: Returns a random quit message when called.
    """
    quit_messages = [
        "I wouldn't leave if I were you. The terminal is much worse.",
        "Don't leave yet. There's a demon around that corner.",
        "Ya know, next time you come in here I'm gonna toast ya.",
        "Go ahead and leave. See if I care.",
        "Are you sure you want to quit this great launcher?",
        "You want to quit? Then, thou hast lost an eighth!",
        "Get outta here and go back to your boring life!",
        "I'm sure you'll be back soon.",
        "Give me ten push-ups, then we'll talk.",
        "I'm too tough to die!",    
        "You cannot quit now. You are one of the Shadow Warriors!",
        "Hmmm, you're a smart marine. You'll hang around here forever.",
        "Chickening out, eh? Okay, I'll let you go ... this time!",
        "Come back here, you coward! We need your brain!",
        "I guess you don't want to see my big secret then?",
        "Don't go now, there's a dimensional shambler waiting for you!",
        "You're trying to say you don't want to play anymore??",
        "It's not time to go yet. We still have much work to do.",
        "Don't leave yet. There's still so much to do!",
        "You're lucky I don't smack you for thinking about leaving.",
    ]
    return quit_messages[int(time()) % 20]
