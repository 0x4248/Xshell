import os
import logging
START_DIR = os.getcwd()
logging.basicConfig(format='[%(asctime)s]  [%(filename)s:%(lineno)d] [ %(levelname)s ]  %(message)s',datefmt='%d-%m-%Y:%H:%M:%S',level=logging.DEBUG,filename='system/temp/logs/System/command.log')
global log
log = logging.getLogger(__name__)
def read(dir):
    """Reads a Registry

    Args:
        dir ([STR]): [Local Xshell dir of the dir e.g system\REGISTRY\LOCAL_SYSTEM\System\SYS_VER\SYS_VER.data]
    """
    regpath = START_DIR+"/"+dir
    try:
        reg = open(regpath,"r")
        out = reg.read()
        reg.close()
        log.info("REGISTRY READ: "+dir)
        return out
    except FileNotFoundError:
        log.error("REGISTRY ERROR: Can't read registry result of 404 DIR:"+dir)
        return "404"
def write(dir,data):
    """write's a Registry

    Args:
        dir ([STR]): [Local Xshell dir of the dir e.g system\REGISTRY\LOCAL_SYSTEM\System\SYS_VER\SYS_VER.data]
    """
    try:
        regpath = START_DIR+"/"+dir
        reg = open(regpath,"w")
        reg.write(data)
        reg.close()
        log.info("REGISTRY WRITE: DIR:"+dir+" DATA:"+data)
    except FileNotFoundError:
        log.error("REGISTRY ERROR: Can't write registry result of 404 DIR:"+dir)
        return "404"        
    