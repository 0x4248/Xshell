def run_addon(name , command):
    from system.system64.syscore import REGISTRY
    import sys
    import os
    
    START_DIR = REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/PATH/START_DIR/START_DIR.reg")
    sys.path.append(START_DIR+"/system/system64/addons")
    x = os.listdir(START_DIR+"/system/system64/addons")
    for i in x:
        if name in i:
            if i.endswith(".py") == True:
               i = i.replace(".py","")
               addon = __import__(i, globals(), locals(), [], 0)
               addon.main(command)
               sys.path.remove(START_DIR+"/system/system64/addons")
               return True
    sys.path.remove(START_DIR+"/system/system64/addons")
    return False