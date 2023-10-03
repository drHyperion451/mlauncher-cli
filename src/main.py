from textual.app import App, ComposeResult
from textual.containers import Grid, Horizontal
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Placeholder, Label, Button

from time import time

QUICK_EXIT = False
# Note: CSS id SHOULD be the same name as the class... wasted 2h of my life


class MenuHeader(Static):
    DEFAULT_CSS = """
    MenuHeader {
        height: 3;
        dock: top;
        content-align: right middle;
    }
    #menuQuitButton {
        dock: right;
        margin-right: 0
    }
    .menuButtons {
        height: 3;
        margin-right: 1
    }

    """
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Button("Game", "primary", id="buttonGame", classes='menuButtons'),
            Button("Wads", "primary", id="wadsButton", classes='menuButtons'),
            Button("Options", "primary", id="optionsButton", classes='menuButtons', disabled=True,),
            Button("Quit", "error", id="menuQuitButton", classes='menuButtons')
        )
class pwadList(Placeholder):
    DEFAULT_CSS= """
    pwadList {
        width: 20
    }
    """
    pass
class pwadDesc(Placeholder):
    DEFAULT_CSS = """
    pwadDesc {
    }
    """
    
class pwadMain(Screen):
    CSS = """
    pwadMain {
    }

    """
    def compose(self) -> ComposeResult:
        yield Horizontal(
            pwadList(id='pwadList'),
            pwadDesc(id='pwadDesc')
        )
            

class MLauncherApp(App):
    """Main Textual App for MLauncher."""

    BINDINGS = [("q", "request_quit", "Quit"), 
                ("d", "toggle_dark", "Dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True, name="Master Launcher", id='header')
        yield MenuHeader(id='MenuHeader')
        yield pwadMain(id='pwadMain')
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
    
    def action_request_quit(self) -> None:
        """ Action that quits the app."""
        if QUICK_EXIT: self.app.exit()
        self.push_screen(QuitScreen())

class QuitScreen(Screen):
    CSS_PATH = 'css/quit.tcss'
    def compose(self) -> ComposeResult:
        yield Grid(
            Label(QuitMsg(), id="question"),
            Button("Quit", variant='error', id="buttonQuit"),
            Button("Cancel", variant='primary', id='buttonCancel'),
            id='closeDialog'
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'buttonQuit':
            self.app.exit()
        else:
            self.app.pop_screen()
def QuitMsg() -> str:
    """Funny Doom II tribute.

    Returns:
        str: Returns a random quit message when called.
    """
    quit_messages = [
        "I wouldn't leave if I were you. DOS is much worse.",
        "Don't leave yet. There's a demon around that corner.",
        "Ya know, next time you come in here I'm gonna toast ya.",
        "Go ahead and leave. See if I care.",
        "Are you sure you want to quit this great game?",
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


if __name__ == '__main__':
    app = MLauncherApp()
    app.run()