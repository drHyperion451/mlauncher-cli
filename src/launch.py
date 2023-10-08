import subprocess
from shlex import split as shlex_split


def game (sourcePort:str, iwad:str, extraPwads='', extra_args='') -> str:

    cmdString = f"{sourcePort} -iwad {iwad}"
    if extra_args != '':
        # Adds arguments plus a space just if the user provides one.
        cmdString = f"{cmdString} {extra_args}"
    
    if extraPwads != '':
        cmdString = f"{cmdString} -file {extraPwads}"

    debug = shlex_split(cmdString)
    cmdList = shlex_split(cmdString)

    for listElement in cmdList: # Makes each element between ("") so spaces
                                # doesn't matter

        listelement = f"\"{listElement}\""

    # print("Command: ", cmdList)
    try:
        stdout = subprocess.run(cmdList, capture_output=True, text=True).stdout
    except (FileNotFoundError, UnboundLocalError):
        # UnboundLocalError mostly is related to FileNotFoundError, so can be passed
        # print("FileNotFoundError: [Errno 2] No such file or directory at line 44"
        pass

    # return stdout                     This gives me errors only in pyinstaller

