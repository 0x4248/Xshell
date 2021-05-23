def get_lang():
    lang = open("system/config/language/lang.config","r")
    x = lang.read()
    return x

def get_sys_ver():
    from system.system64.syscore import REGISTRY
    z = REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/System/SYS_VER/SYS_VER.data")
    z = z[:6]
    return z

def get_build_ver():
    from system.system64.syscore import REGISTRY
    z = REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/System/SYS_BUILD/VER.data")
    z = z[:18]
    return z

def get_welcome_message():
    lang = get_lang()
    if lang == "en-uk":
        x = open("system/config/welcome/en-uk/welcome.lang","r")
        z = x.read()
        return z
    if lang == "en-us":
        x = open("system/config/welcome/en-us/welcome.lang","r")
        z = x.read()
        return z