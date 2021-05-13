global install
install = []
import os
def check_installed_modules():
    try:
        import colr
    except:
        install.append("colr")
    try:
        import requests
    except:
        install.append("requests")
    try:
        import pythonping
    except:
        install.append("pythonping")
    try:
        import js2py
    except:
        install.append("js2py")

check_installed_modules()
if install == []:
    print("Nothing needs to be installed now just run Xshell")
    input("press enter to quit...")
    exit()

consent = input("Xshell installer found some dependencies that need to be installed \nDo you want to install them Y or N?")
consent = consent.upper()
if consent == "Y":
    pass
if consent != "Y":
    print("[X] Xshell installer will now quit no changes were made")
    input("press enter to quit...")
    exit() 

for i in install:
    print("[INSTALL] "+i)
for i in install:
    try:
        x = "pip install "+i
        os.system(x)
    except:
        print("[SKIP] An error prevented this module from being installed ")
for i in install:
    try:
        x = "pip3 install "+i
        os.system(x)
    except:
        print("[SKIP] An error prevented this module from being installed ")
print("Xshell has installed the dependencies")
input("press enter to quit...")
exit()