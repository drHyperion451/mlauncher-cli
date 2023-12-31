Rem Maybe you need to run this on PS:  Set-ExecutionPolicy Unrestricted -Scope Process 
Rem #pyright: reportUndefinedVariable=false at the top of any python file will ignore imports
 
pyinstaller src/main.py -y -D --add-data src/ml_info.json:src --add-data src/css/mlauncher.tcss:css -n MLauncher --paths=.\pyenv\Lib\site-packages

copy README.MD dist\MLauncher\README.MD
copy COPYING dist\MLauncher\COPYING