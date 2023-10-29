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

from globals import *

# Note: CSS id SHOULD be the same name as the class... wasted 2h of my life

class MenuHeader(Static):
    """ Top bar menu static Widget """

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Button("Game", "primary", id="buttonGame", classes='menuButtons', disabled=True),
            Button("Wads", "primary", id="wadsButton", classes='menuButtons', disabled=True),
            Button("Options", "primary", id="optionsButton", classes='menuButtons', disabled=True),
            Button("Quit", "error", id="menuQuitButton", classes='menuButtons')
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "buttonGame":
                pass
            case "wadsButton":
                pass
            case "optionsButton":
                self.app.push_screen(OptionsScreen(classes='DialogScreen'))
            case "menuQuitButton":
                self.app.push_screen(QuitScreen(classes='DialogScreen'))

class OptionsScreen(Screen):
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
        self.push_screen(QuitScreen(classes='DialogScreen'))


if __name__ == '__main__':
    # Renames terminal tab if avaliable:
    sys.stdout.write("\x1b]2;%s\x07" % 'MLauncher')

    # Loads config file or creates it with default info:
    config = configparser.ConfigParser()
    if not os.path.exists('config.ini'):
        config['GAME'] = {'SOURCEPORT': './dsda-doom/dsda-doom.exe',
                        'IWAD': './doom2/DOOM2.WAD',
                        'ML_PATH': './master/wads'}
        
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    config.read('config.ini')

    maps = jsonUtils.MapsJson(JSON_FILEPATH)
    SOURCEPORT = config.get('GAME', 'SOURCEPORT')
    IWAD = config.get('GAME', 'IWAD')
    ML_PATH = config.get('GAME', 'ML_PATH')

    MLauncherApp().run()

