from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Header, Footer, Static, Button, Placeholder

import os
from configparser import ConfigParser

# MODULES:
from i_system import openFile, str_to_bool
from i_infoWidgets import *
import g_launch


from ui_pwad_launch_options import pwadLaunchOptions
from globals import GlobalVars, SETTINGS_PATH

# SCREENS:
from s_game import GameScreen
from s_wads import WadsScreen
from s_settings import SettingsScreen
from s_quit import QuitScreen

# Note: CSS id SHOULD be the same name as the class... wasted 2h of my life

class MenuHeader(Static):
    """ Top bar menu static Widget """

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Button("Game", "primary", id="gameButton", classes='menuButtons', disabled=False),
            Button("Wads", "primary", id="wadsButton", classes='menuButtons', disabled=False),
            Button("Options", "primary", id="optionsButton", classes='menuButtons', disabled=False),
            #Button("Console Output", "warning", id="consoleLogButton", classes='menuButtons', disabled=False),
            Button("Quit", "error", id="menuQuitButton", classes='menuButtons')
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "gameButton":
                self.app.push_screen(GameScreen(id='gameScreen', classes='DialogScreen'))
            case "wadsButton":
                self.app.push_screen(WadsScreen(id='wadsScreen', classes='DialogScreen'))
            case "optionsButton":
                openFile(SETTINGS_PATH)
                #self.app.push_screen(SettingsScreen(classes='DialogScreen'))
            case "menuQuitButton":
                self.app.push_screen(QuitScreen(classes='DialogScreen'))

    
class pwadMain(Static):
    CSS_PATH = 'css/pwadMain.tcss'
    def compose(self) -> ComposeResult:
        yield Horizontal(
            pwadList(id='pwadList'),
            pwadContents(id='pwadContents')
        )
    # WADS LIST HANDLER:
    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Refresh if the user selects map:
        if 'map-buttons' in event.button.classes:
            GlobalVars.SELECTED_MAP = event.button.id + '.WAD'
            # Change the title
            self.query_one("#title").str_body = GlobalVars.SELECTED_MAP
            self.query_one('#author').str_body = maps.get_from_data('WAD', GlobalVars.SELECTED_MAP, 'Author')[0]
            # Change WARP_PC:
            GlobalVars.WARP_PC = maps.get_from_data('WAD', GlobalVars.SELECTED_MAP, 'PC')[0]
            
class pwadList(VerticalScroll):

    def compose(self) -> ComposeResult:
        wads = maps.get_all_wads_ordered(GlobalVars.WADS_ORDER, displayExtension=False)

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
        yield pwadLaunchOptions(id='pwadLaunchOptions')
        yield Button("LAUNCH", variant='success', id='launchButton')
    
    #  LAUNCH HANDLER:
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'launchButton':
            if GlobalVars.SELECTED_MAP:
                master_wad = f"{GlobalVars.ML_PATH}/{GlobalVars.SELECTED_MAP}"
                g_launch.game(GlobalVars.SOURCEPORT, GlobalVars.IWAD, master_wad)
                config.set('GAME', 'SELECTED_MAP', GlobalVars.SELECTED_MAP)
                config.set('GAME', 'SKILL', str(GlobalVars.SKILL))
                #config.set('GAME', 'WARP', WARP)
                with open(SETTINGS_PATH, 'w') as configfile:
                    config.write(configfile)


class MLauncherApp(App):
    """Main Textual App for MLauncher."""
    CSS_PATH = './css/mlauncher.tcss'
    BINDINGS = [("q", "request_quit", "Quit"), 
                ("d", "toggle_dark", "Dark mode"),
                ("s", "request_settings", "Settings")]
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
        
        if str_to_bool(GlobalVars.QUICK_EXIT):
            self.app.exit()
        self.push_screen(QuitScreen(classes='DialogScreen'))

    def action_request_settings(self) -> None:
        """ Action that opens SettingsScreen"""
        self.push_screen(SettingsScreen(classes='DialogScreen'))

if __name__ == '__main__':
    # Renames terminal tab if avaliable:
    sys.stdout.write("\x1b]2;%s\x07" % 'MLauncher')

    # CWD to executable 
    if getattr(sys, 'frozen', False):
        os.chdir(os.path.dirname(sys.executable))
    

    # Loads config file or creates it with default info:
    
    config = ConfigParser()
    config.read(filenames= SETTINGS_PATH)

    MLauncherApp().run()

