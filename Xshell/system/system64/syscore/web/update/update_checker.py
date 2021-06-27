def check_ver(say=False):
    import urllib.request
    from system.system64.syscore import REGISTRY
    contents = urllib.request.urlopen("https://raw.githubusercontent.com/awesomelewis2007/Xshell/main/Xshell/system/REGISTRY/LOCAL_SYSTEM/SYSTEM/SYS_VER/SYS_VER.data").read()
    current_ver = contents.decode("utf-8")
    this_ver = REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/SYS_VER/SYS_VER.data")
    current_ver =  current_ver[:6]
    this_ver = this_ver[:6]
    if say == True:
        if this_ver != current_ver:
            from colr import color
            print("There is a newer version for Xshell")
            print(color(this_ver,fore="red")+"==>"+color(current_ver,fore="green"))
            url = "https://github.com/awesomelewis2007/Xshell/releases/tag/"+current_ver
            print("You can download this update at: "+color(url,fore="cyan"))
            return True
        if this_ver == current_ver:
            return False    
    if say == False:
        if this_ver != current_ver:
            return True
        if this_ver == current_ver:
            return False      
