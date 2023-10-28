pyinstaller src/main.py -y -F --add-data src/ml_info.json:src --add-data src/css/mlauncher.tcss:css -n 'MLauncher' --paths='/usr/local/lib/python3.11/site-packages'

#./dist/MLauncher/MLauncher
