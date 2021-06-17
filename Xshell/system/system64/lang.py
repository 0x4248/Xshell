def get_lang():
    lang = open("system/config/language/lang.config","r")
    x = lang.read()
    return x

def get_sys_ver():
    from system.system64.syscore import REGISTRY
    z = REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/SYS_VER/SYS_VER.data")
    z = z[:6]
    return z

def get_build_ver():
    from system.system64.syscore import REGISTRY
    z = REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/SYS_BUILD/VER.data")
    z = z[:18]
    return z

def get_welcome_message():
    x = open("system/config/welcome/welcome","r")
    z = x.read()
    return z