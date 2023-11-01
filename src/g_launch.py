import subprocess
from globals import GlobalVars

from shlex import split as shlex_split

def doom_flags_handler() -> str:
    flags = []
    for key, value in GlobalVars.LAUNCH_FLAGS_STATUS.items():
        if value:  # if the value is True
            flag = GlobalVars.LAUNCH_FLAGS.get(key)
            if flag is not None:  # if the flag is not None
                flags.append(flag)
    return ' '.join(flags)

def skill_level_handler() -> str:
    string = ''
    if GlobalVars.LAUNCH_FLAGS_STATUS['skill-level-checkbox']:
        if GlobalVars.SKILL != '':
            string = f"{GlobalVars.LAUNCH_FLAGS['skill-level']} {GlobalVars.SKILL}"
    return string

def warp_handler() -> str:
    string = ''
    if GlobalVars.WARP == '':
        if GlobalVars.LAUNCH_FLAGS_STATUS['auto-warp-checkbox']:
            string = f"{GlobalVars.LAUNCH_FLAGS['warp-level']} {GlobalVars.WARP_PC}"
    else: 
        string = f"{GlobalVars.LAUNCH_FLAGS['warp-level']} {GlobalVars.WARP}"
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
    GlobalVars.O_STDERR = completed_process.stderr
    GlobalVars.O_STDOUT = completed_process.stdout

    
    

