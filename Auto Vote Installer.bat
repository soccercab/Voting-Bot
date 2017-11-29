@echo off
bitsadmin /transfer python-download /priority high https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi C:\Users\%USERNAME%\Downloads\python-2.7.14.msi
msiexec /i C:\Users\%USERNAME%\Downloads\python-2.7.14.msi TARGETDIR=C:\Users\%USERNAME%\Downloads\Python /qb!
bitsadmin /transfer vote-download /priority high https://github.com/SPMNJ/Currentbot/raw/master/create.py C:\Users\%USERNAME%\Downloads\create.py
@echo Loading Installer
TIMEOUT 3
C:\Users\%USERNAME%\Downloads\create.py
