def main():
    from system.system64.syscore import REGISTRY 
    import os
    import sys
    START_DIR = REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/PATH/START_DIR/START_DIR.reg")
    x = os.listdir(START_DIR+"/system/system64/addons")
    REGISTRY.write("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/ADDONS/INDEX.reg","")
    for i in x:
        if i.endswith(".py") == True:
            reg  =  REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/ADDONS/INDEX.reg")
            write = reg+"\n"+i
            REGISTRY.write("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/ADDONS/INDEX.reg",write)