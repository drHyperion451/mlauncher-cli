from textual.app import ComposeResult
from textual.containers import Grid, Horizontal
from textual.screen import Screen
from textual.widgets import Button, Footer, Markdown

from i_system import openBrowser

about_markdown_message = """\
# MASTER LEVELS LAUNCHER: 
A TUI launcher made for Master Levels of Doom II
### Purchase DOOM II
* [Steam](https://store.steampowered.com/app/2300/DOOM_II/)
* [GOG](https://www.gog.com/en/game/doom_ii)
## GPL v3 License:
MLauncher
Copyright (C) 2023  drHyperion451

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

class AboutScreen(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]
    def compose(self) -> ComposeResult:
        yield Grid(
            Horizontal(
                Button("Source Code", "primary", id='source-code-button'),
                Button("Support Me!", "error", id='support-button'),
                id='about-buttons',
                classes='md-center'

            ),
            Markdown(about_markdown_message),
            id='about-dialog',
            classes='dialogGrid md-center'
        )
        yield Footer()
    def on_markdown_link_clicked(self, event: Markdown.LinkClicked) -> None:
        openBrowser(event.href)
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case 'source-code-button':
                openBrowser('https://github.com/drHyperion451/mlauncher-cli')
            case 'support-button':
                openBrowser('https://ko-fi.com/drhyperion451')
