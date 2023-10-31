import subprocess
from globals import *
from shlex import split as shlex_split

def doom_flags_handler() -> str:
    flags = []
    for key, value in LAUNCH_FLAGS_STATUS.items():
        if value:  # if the value is True
            flag = LAUNCH_FLAGS.get(key)
            if flag is not None:  # if the flag is not None
                flags.append(flag)
    return ' '.join(flags)

def skill_level_handler() -> str:
    string = ''
    if LAUNCH_FLAGS_STATUS['skill-level-checkbox']:
        if SKILL != '':
            string = f"{LAUNCH_FLAGS['skill-level']} {SKILL}"
    return string

def warp_handler() -> str:
    string = ''
    global WARP
    if WARP == '':
        if LAUNCH_FLAGS_STATUS['auto-warp-checkbox']:
            string = f"{LAUNCH_FLAGS['warp-level']} {WARP_PC}"
    else: 
        string = f"{LAUNCH_FLAGS['warp-level']} {WARP}"
    return string
    

def game (sourcePort:str, iwad:str, extraPwads:str | None = None) -> str:

    cmdString = f"{sourcePort} -iwad {iwad}"
    if extraPwads != None:
        cmdString += f" -file {extraPwads}"

    cmdString += f' {doom_flags_handler()} {skill_level_handler()} {warp_handler()}'
    # Splits into arguments. Just because subprocess.run needs this.
    cmdList = shlex_split(cmdString)


    completed_process = subprocess.run(cmdList, capture_output=True, text=True)
    
    # This will handle properly if errors had happened or not.
    O_STDERR = completed_process.stderr
    O_STDOUT = completed_process.stdout
    O_STDOUT, O_STDERR, cmdList
    
    

