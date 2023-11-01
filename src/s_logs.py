from textual.app import ComposeResult
from textual.containers import Grid, Container
from textual.screen import Screen
from textual.widgets import Footer, Markdown

from globals import GlobalVars



class LogsScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]
    def compose(self) -> ComposeResult:
        n = 2.4 # Higher the number the shorter it gets

        yield Grid(
            Container(
                Markdown(GlobalVars.O_STDERR, id='err_log')
            ),
            Container(
                Markdown(GlobalVars.O_STDOUT, id='def_log')
            ),
            id='logs-dialog',
            classes='dialogGrid md-center'
        )
        yield Footer()
