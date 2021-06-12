import os
from re import IGNORECASE
from system.system64.syscore import REGISTRY
wd = os.getcwd()
def read():  
    f = open(wd+"/"+"system/temp/history","r")
    x = f.read()
    ignore = REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/HISTORY/IGNORE.data")
    x = x.replace(ignore,"")
    print(x)
    f.close()
def clear():
    f = open(wd+"/"+"system/temp/history","w")
    start_file = REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/HISTORY/START_FILE.data")
    f.write(start_file)
    f.close()
def write(command):
    f = open(wd+"/"+"system/temp/history","a")
    f.write("\n"+command)
    f.close()
def set_to(x):
    """
    1 for history to be on
    0 for history to be off
    """
    if x == "0":
        REGISTRY.write("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/HISTORY/HISTORY_ON.data","0")
    if x == "1":
        REGISTRY.write("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/HISTORY/HISTORY_ON.data","1")