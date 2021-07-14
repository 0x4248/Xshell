def main():
    # Temp Clear module
    from colr import color
    import os
    import shutil
    print(color("[!] Warning this will clear all temp including your",fore="yellow")+color("history",fore="red"))
    print("Note: Xshell may not be responsive or crash at any moment if this is done!")
    consent = input("press enter to continue or type exit to quit:")
    consent = consent.upper()
    if consent == "EXIT":
        return None
    dir = os.listdir("system/temp")
    for i in dir:
        path = "system/temp"+"/"+str(i)
        print("Removing History")
        from system.system64.syscore import history
        history.clear()
        print("Removing File:"+path)
        try:
            shutil.move(path,"system\SYSTEM_TRASH")
        except PermissionError:
            print(color("[X] The File:"+path+" can not be removed due to a permmition error 401", fore="red"))
            print("Try removing the file without Xshell Running")
        except FileNotFoundError:
            print(color("[X] The File:"+path+" can not be removed due to a file not found error 404", fore="red"))
        except FileExistsError:
            print(color("[X] The File:"+path+" can not be removed due to file is already in the SYSTEM_TRASH folder 406", fore="red"))  
        except:
            print(color("[X] The File:"+path+" can not be removed due to an unknown error in the system", fore="red"))  
    return None
