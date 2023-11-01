# MLauncher: Master Launcher
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<div style="text-align:center">
<b style="color:crimson;">This project is still on pre-apha. Please, be nice! :)</b>
</div>

![Windows Screenshot](https://github.com/drHyperion451/mlauncher-cli/blob/master/assets/screenshot1.png?raw=true)

A cross-platform, classic style DOOM launcher for [Master Levels for DOOM II](https://store.steampowered.com/app/9160/Master_Levels_for_Doom_II/).
:feelsgood:
## Getting Started
This proyect runs using the [`Textual`](https://textual.textualize.io) Python library to run. It should work with the compiled release, but due to python being an interpreted language it should by using the source and the python IDLE.
### Prerequisites:
- Any compatible **Doom launcher**. [*DSDA-Doom*](https://github.com/kraflab/dsda-doom) is highly recommended but you can use any of them **as long as it's compatible**.
- Have a copy of Master Levels for DOOMII. You can purchase it through [Steam](https://login.steampowered.com/jwt/refresh?redir=https://store.steampowered.com/app/9160/Master_Levels_for_Doom_II/) or [GOG](https://www.gog.com/game/doom_ii)
- *Optional*: [iTerm2](https://iterm2.com/) for MacOS or [Windows Terminal](https://www.microsoft.com/store/productId/9N0DX20HK701?ocid=pdpshare). Default Windows Powershell or cmd.exe surprisingly looks very cool, but if you want a cleaner experience **I recommend** installing this.

### Installation:
This program is made to work and launch with the Steam release using [*DSDA-Doom*](https://github.com/kraflab/dsda-doom), but it includes a config file. See [Configuration](#configuration) for more info.

1. Get the latest MLauncher release from the [releases tab](https://github.com/drHyperion451/mlauncher-cli/releases/latest) at your right. Download the one that suits you well.

2. Go to the main game directory for "Master Levels for Doom 2". [Guide on how to look it.](https://jstationx.com/how-to-get-into-game-files-on-steam/)

3. Extract both files (`_internal` and `MLauncher.exe`) inside the main game directory.

4. Rename `doxbox.exe` to `dosbox.exe.old`. Rename `Mlauncher.exe` to `dosbox.exe`. This will trick steam on loading this program instead of dosbox. Keep the old dosbox as backup.

5. Go to [dsda-doom](https://github.com/kraflab/dsda-doom) repository and download or compile your binaries. Read their README.md file to find out useful info.

6. Extract the dsda-doom zip inside `Master Levels of Doom\dsda-doom\` directory. Please **extract it inside a directory!**. The source port executable should be at `.\dsda-doom\dsda-doom.exe`

You are good to go! If you have any problems, check the configuration file inside `config.ini` created inside the game folder. I've ended up with this tree inside the main game folder:

```
Master Levels of Doom
│   AUTHORS.txt
│   config.ini
│   COPYING.txt
│   dosbox-0.71.tar.gz
│   dosbox.conf
│   dosbox.exe
│   dosbox.exe.old
│   INSTALL.txt
│   master.bat
│   master.conf
│   NEWS.txt
│   README.txt
│   SDL.dll
│   SDL_net.dll
│   testapp.bat
│   THANKS.txt
│   uninstall.exe
├───capture
├───doom2
├───dsda-doom
├───master
├───zmbv
│       README.txt
│       zmbv.dll
│       zmbv.inf
└───_internal
```

## Configuration:
Inside `config.ini` file the info is organized inside keys. GUI settings are planned but not avaliable yet, please wait!.
- `sourceport` = Relative path to your favorite source port. By default is set to `.\dsda-doom\dsda-doom.exe`.
- `iwad` = Relative path of DOOM2 iwad. Default is: `./doom2/DOOM2.WAD`
- `ml_path` = Relative path of all the wads. Default is `./master/wads`


### Building
Building is a mess right now because of some differences between OS and Textual not been detected by default on my system. A work is on the way to fix this.

1. Clone this repository and open a terminal inside the folder. Creating a virtual environment is very recommended if you don't want to install extra apps on your system.
2. Install `python 3.11` and `pyinstaller` using your package manager or other ways. Make sure it's on the terminal PATH.
3. Run `pip3 install -r requirements.txt`
4. Run `python3.11 src/main.py` and make sure if it works correctly.
5. If you want to freeze the proyect, run `pyinstaller build.sh`. or use `build.bat` instead on Windows.


[contributors-shield]: https://img.shields.io/github/contributors/drHyperion451/mlauncher-cli.svg?style=for-the-badge
[contributors-url]: https://github.com/drHyperion451/mlauncher-cli/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/drHyperion451/mlauncher-cli.svg?style=for-the-badge
[forks-url]: https://github.com/drHyperion451/mlauncher-cli/network/members
[stars-shield]: https://img.shields.io/github/stars/drHyperion451/mlauncher-cli.svg?style=for-the-badge
[stars-url]: https://github.com/drHyperion451/mlauncher-cli/stargazers
[issues-shield]: https://img.shields.io/github/issues/drHyperion451/mlauncher-cli.svg?style=for-the-badge
[issues-url]: https://github.com/drHyperion451/mlauncher-cli/issues
[license-shield]: https://img.shields.io/github/license/drHyperion451/mlauncher-cli.svg?style=for-the-badge
[license-url]: https://github.com/drHyperion451/mlauncher-cli/blob/master/COPYING
