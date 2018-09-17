@echo off
set lol=%USERNAME%
@echo Installing for user: %lol%
bitsadmin /Cancel python-download
bitsadmin /cancel votescript-download
bitsadmin /transfer python-download https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi C:\Users\%lol%\Downloads\python-2.7.15.msi
msiexec /i C:\Users\%lol%\Downloads\python-2.7.15.msi TARGETDIR=C:\Users\%lol%\Downloads\Python /qb!
bitsadmin /transfer votescript-download https://github.com/soccercab/Voting-Bot/blob/master/install.py C:\Users\%lol%\Downloads\install.py
bitsadmin /transfer votescript-download https://github.com/soccercab/Voting-Bot/blob/master/Requests.bat C:\requests.bat
@echo Loading Installer
C:\Users\%lol%\Downloads\install.py
