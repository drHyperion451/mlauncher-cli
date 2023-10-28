site_packages=$(python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')

PYTHONOPTIMIZE=2 pyinstaller src/main.py -y -D --add-data src/ml_info.json:src --add-data src/css/mlauncher.tcss:css -n 'MLauncher' --paths=$site_packages

#./dist/MLauncher/MLauncher
