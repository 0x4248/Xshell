def get_path():
    import sys
    x = sys.path
    return x
def add_path(x):
    import sys
    sys.path.append(x)

def remove_path(x):
    import sys
    try:
        sys.path.remove(x)
    except:
        return "ERROR"
def main():
    from system.system64.syscore import REGISTRY
    ver = REGISTRY.read("system\REGISTRY\LOCAL_SYSTEM\PATH\VER")
    print("Welcome to path Ver:"+ver)
    while True:
        command = input("PATH>>")
        if "add " in command:
            ccomand = command[:3]
            if ccomand == "add":
                command = command.replace("add ","")
                import sys
                sys.path.append(command)
                print("added",command)
        if "remove " in command:
            ccomand = command[:6]
            if ccomand == "remove":
                command = command.replace("remove ","")
                import sys
                sys.path.remove(command)
                print("removed",command)

        if "list" in command:
            import sys
            x = sys.path
            for i in x:
                print(i)

        if "exit" in command:
            break
