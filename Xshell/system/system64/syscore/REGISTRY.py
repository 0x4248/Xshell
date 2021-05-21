import os
START_DIR = os.getcwd()
def read(dir):
    """Reads a Registry

    Args:
        dir ([STR]): [Local Xshell dir of the dir e.g system\REGISTRY\LOCAL_SYSTEM\System\SYS_VER\SYS_VER.data]
    """
    regpath = START_DIR+"/"+dir
    try:
        reg = open(regpath,"r")
        out = reg.read()
        reg.close() #removes the file from the python39 memory for security 
        return out
    except FileNotFoundError:
        return "404"
def write(dir,data):
    """write's a Registry

    Args:
        dir ([STR]): [Local Xshell dir of the dir e.g system\REGISTRY\LOCAL_SYSTEM\System\SYS_VER\SYS_VER.data]
    """
    regpath = START_DIR+"/"+dir
    reg = open(regpath,"w")
    reg.write(data)
    reg.close() #removes the file from the python39 memory for security 
    