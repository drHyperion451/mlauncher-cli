import platform
import os
import webbrowser
OS = platform.system()

def openFile(filePath):
    match OS:
        case 'Windows' | 'Linux': # TODO: Linux works?
            webbrowser.open(filePath)
        case 'Darwin':
            os.system(f'open {filePath}')

def str_to_bool(s:str) -> bool:
    """Parses string to bool

    Args:
        s (str): String to parse. Must be either 'False' or 'True'

    Raises:
        Parsing string error: Created if the string isn't 'False' nor 'True'

    Returns:
        bool: Bool return.
    """
    match s:
        case 'False':
            return False
        case 'True':
            return True
        case _:
            raise Exception('str_to_bool error: Parsing string error')