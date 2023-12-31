import platform
import os
import webbrowser
import textwrap

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

def openBrowser(url:str) -> None:
    match OS:
        case 'Windows' | 'Linux':
            webbrowser.open_new_tab(url)
        case 'Darwin':
            os.system(f'open {url}')

def wrap_text(text, width):
    lines = text.split('\n')
    wrapped_lines = [textwrap.wrap(line, width) for line in lines]
    wrapped_text = '\n'.join(['\n'.join(line) for line in wrapped_lines])
    return wrapped_text