# MLauncher: Master Launcher
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


A cross-platform, classic style DOOM launcher for [Master Levels for DOOM II](https://store.steampowered.com/app/9160/Master_Levels_for_Doom_II/).

## Getting Started
This proyect runs using the [`Textual`](https://textual.textualize.io) Python library to run. It should work with the compiled release, but due to python being an interpreted language it should by using the source and the python IDLE.
### Prerequisites:
- Any compatible **Doom launcher**. [*DSDA-Doom*](https://github.com/kraflab/dsda-doom) is highly recommended but you can use any of them **as long as it's compatible**.
- Have a copy of Master Levels for DOOMII. You can purchase it through [Steam](https://login.steampowered.com/jwt/refresh?redir=https://store.steampowered.com/app/9160/Master_Levels_for_Doom_II/) or [GOG](https://www.gog.com/game/doom_ii)
### Building
1. Clone this repository and open a terminal inside the folder. Creating a virtual environment is very recommended if you don't want to install extra apps on your system.
2. Install `python 3.11` and `pyinstaller` using your package manager or other ways. Make sure it's on the terminal PATH.
3. Run `pip3 install -r requirements.txt`
4. Run `python3.11 src/main.py` and make sure if it works correctly.
5. If you want to freeze the proyect, run `pyinstaller main.spec`. Use `-f` flag if you want onefile (but it runs slow the first time you launch)

[contributors-shield]: https://img.shields.io/github/contributors/drHyperion451/MLauncher.svg?style=for-the-badge
[contributors-url]: https://github.com/drHyperion451/MLauncher/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/drHyperion451/MLauncher.svg?style=for-the-badge
[forks-url]: https://github.com/drHyperion451/MLauncher/network/members
[stars-shield]: https://img.shields.io/github/stars/drHyperion451/MLauncher.svg?style=for-the-badge
[stars-url]: https://github.com/drHyperion451/MLauncher/stargazers
[issues-shield]: https://img.shields.io/github/issues/drHyperion451/MLauncher.svg?style=for-the-badge
[issues-url]: https://github.com/drHyperion451/MLauncher/issues
[license-shield]: https://img.shields.io/github/license/drHyperion451/MLauncher.svg?style=for-the-badge
[license-url]: https://github.com/drHyperion451/MLauncher/blob/master/COPYIING
