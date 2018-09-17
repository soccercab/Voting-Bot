@echo off
set lol=%USERNAME%
@echo Installing for user: %lol%
bitsadmin /cancel votescript-download
bitsadmin /cancel requests-download
msiexec /i C:\Users\%lol%\Downloads\python-2.7.15.msi TARGETDIR=C:\Users\%lol%\Downloads\Python /qb!
bitsadmin /transfer votescript-download https://github.com/SPMNJ/Voting-Bot/raw/master/install.py C:\Users\%lol%\Downloads\install.py
bitsadmin /transfer requests-download https://github.com/SPMNJ/Voting-Bot/raw/master/requests.bat %localappdata%\Temp\requests.bat
@echo Loading Installer
C:\Users\%lol%\Downloads\install.py
