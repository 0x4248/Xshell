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
check_installed_modules()
if install == []:
    print("Nothing needs to be installed now just run Xshell")
    exit()

consent = input("Xshell installer found some dependencies that need to be installed \nDo you want to install them Y or N?")
consent = consent.upper()
if consent == "Y":
    pass
if consent != "Y":
    print("[X] Exit")
    exit() 

for i in install:
    print("[INSTALL] "+i)
for i in install:
    x = "pip install "+i
    os.system(x)
print("Xshell has installed the dependencies")
exit()