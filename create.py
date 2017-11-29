import urllib
import os
import time
print "Installing..."
urllib.urlretrieve ("https://github.com/SPMNJ/Currentbot/raw/master/install.py", "install.py")
text = ['set WshShell=createobject("wscript.shell")', 'WScript.Sleep 1000', 'WshShell.run "install.py"', '']
code = open("run.vbs","w+")
for i in range(len(text)):
    code.write(text[i]+"\n")
code.close()
os.startfile("run.vbs")
