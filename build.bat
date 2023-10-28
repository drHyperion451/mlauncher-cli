Rem Maybe you need to run this on PS:  Set-ExecutionPolicy Unrestricted -Scope Process 
Rem #pyright: reportUndefinedVariable=false at the top of any python file will ignore imports
 
pyinstaller src/main.py -y -D --add-data src/ml_info.json:src --add-data src/css/mlauncher.tcss:css -n MLauncher --paths=E:\Users\sbritorodr\Documentos\GitHub\mlauncher-cli\pyenv\Lib\site-packages