import platform
import os
import webbrowser
OS = platform.system()

def openFile(filePath):
    match OS:
        case 'Windows', 'Linux': # Check: Linux works?
            webbrowser.open(filePath)
        case 'Darwin':
            os.system(f'open {filePath}')
