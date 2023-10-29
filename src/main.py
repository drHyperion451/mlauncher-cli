from textual.app import App, ComposeResult
from textual.containers import Grid, Horizontal, VerticalScroll
from textual.reactive import reactive
from textual.widget import Widget
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Placeholder, Label, Button, Pretty


import os
import configparser

# MODULES:
import jsonUtils
import launch
from infoWidgets import *
from ui_quit import QuitScreen
from ui_settings import SettingsScreen, Settings
from globals import *

# Note: CSS id SHOULD be the same name as the class... wasted 2h of my life

class MenuHeader(Static):
    """ Top bar menu static Widget """

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Button("Game", "primary", id="buttonGame", classes='menuButtons', disabled=True),
            Button("Wads", "primary", id="wadsButton", classes='menuButtons', disabled=True),
            Button("Options", "primary", id="optionsButton", classes='menuButtons', disabled=False),
            Button("Quit", "error", id="menuQuitButton", classes='menuButtons')
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "buttonGame":
                pass
            case "wadsButton":
                pass
            case "optionsButton":
                self.app.push_screen(SettingsScreen(classes='DialogScreen'))
            case "menuQuitButton":
                self.app.push_screen(QuitScreen(classes='DialogScreen'))

    
class pwadMain(Static):
    CSS_PATH = 'css/pwadMain.tcss'
    def compose(self) -> ComposeResult:
        yield Horizontal(
            pwadList(id='pwadList'),
            pwadContents(id='pwadContents')
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Refresh if the user selects map:
        if 'map-buttons' in event.button.classes:
            global SELECTED_FILE
            SELECTED_FILE = event.button.id + '.WAD'
            # Change the title
            self.query_one("#title").str_body = SELECTED_FILE
            self.query_one('#author').str_body = maps.get_from_data('WAD', SELECTED_FILE, 'Author')[0]

class pwadList(VerticalScroll):

    def compose(self) -> ComposeResult:
        wads = maps.get_all_wads_ordered('PSN', displayExtension=False)

        for eachWad in wads:
            yield Button(eachWad, id=eachWad, classes="map-buttons")
        
    def on_button_pressed(self, event: Button.Pressed):
        pass
        
class pwadInfo(Static):
    def compose(self) -> ComposeResult:
        yield PwadTitle(id='title')
        yield PwadAuthor(id='author')

class pwadContents(Static):
    def compose(self) -> ComposeResult:
        yield pwadInfo()
        yield Button("LAUNCH", variant='success', id='launchButton')

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if SELECTED_FILE:
            master_wad = f"{ML_PATH}/{SELECTED_FILE}"
            launch.game(SOURCEPORT, IWAD, master_wad)


class MLauncherApp(App):
    """Main Textual App for MLauncher."""
    CSS_PATH = './css/mlauncher.tcss'
    BINDINGS = [("q", "request_quit", "Quit"), 
                ("d", "toggle_dark", "Dark mode"),
                ("s", "request_settings", "settings")]
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
        self.push_screen(QuitScreen(classes='DialogScreen'))

    def action_request_settings(self) -> None:
        """ Action that opens SettingsScreen"""
        self.push_screen(SettingsScreen(classes='DialogScreen'))

if __name__ == '__main__':
    # Renames terminal tab if avaliable:
    sys.stdout.write("\x1b]2;%s\x07" % 'MLauncher')
    
    maps = jsonUtils.MapsJson(JSON_FILEPATH)

    # Loads config file or creates it with default info:
    config = Settings('config.ini')
    SOURCEPORT = config.getOption('GAME', 'SOURCEPORT')
    IWAD = config.getOption('GAME', 'IWAD')
    ML_PATH = config.getOption('GAME', 'ML_PATH')

    MLauncherApp().run()

