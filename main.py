class Boot:
    def Fatal_cant_boot(errorno = "Unkown error no",reason = "No reason was given",log = "No log file was found",fix = "No fixes avalible"):
        print("[X] Fatal Xshell cant boot due to an error in the system")
        print("--------------------------------------------------------")
        print("Error Number:",errorno)
        print("Reason:",reason)
        print("Log:")
        print("--------------------------------------------------------")
        print(log)
        print("--------------------------------------------------------")
        print("Fixes:",fix)
        exit()

class Welcome:
    def get_welcome_message():
        from system.system64 import lang
        return lang.get_welcome_message()

    def get_ver():
        from system.system64 import lang
        ver = lang.get_build_ver()
        ver = str(ver)
        return ver

    def get_cpu():
        import platform
        cpu = platform.processor()
        cpu = str(cpu)
        return cpu

    def get_os_type():
        import platform
        system = platform.system()
        system = str(system)
        return system

    def get_os_ver():
        import platform
        ver = platform.version()
        ver = str(ver)
        return ver


class check_system:
    def check_filesystem():
        import os
        from os import path
        import sys
        paths = ["system","system/system64","system/system64/syscore","system/system64/syslib"]
        log = "INFO: Exacuteing sys checkdisk\n"
        for i in paths:
            log = log + "INFO: Checking path '"+i+"\n"
            x = os.path.exists(i)
            if x == True:
                pass
                log = log + "INFO: The path '"+i+"' was found and continuing to next path\n"
                log = log + "\n"
            if x == False:
                log = log + "ERROR: Path not found '"+i+"\n"
                log = log + "-----SYSHALT-----"
                a = "CHECK DISK: The system cant find the path '"+i+"'"
                Boot.Fatal_cant_boot(errorno="404",reason=a,log=log,fix="Reinstall Xshell or relocate the missing path or file")
#=====================MAIN======================

try:
    import os
except:
    Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module os",log="none",fix="try to install the module using pip")
try:
    import sys
except:
    Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module sys",log="none",fix="try to install the module using pip")
try:
    import time
except:
    Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module time",log="none",fix="try to install the module using pip")
try:
    import datetime
except:
    Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module datetime",log="none",fix="try to install the module using pip")
try:
    import platform
except:
    Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module platform",log="none",fix="try to install the module using pip")  
try:
    from colr import color
except:
    Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module colr",log="none",fix="try to install the module using pip") 
try:
    import curses
except:
    Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module curses",log="none",fix="try to install the module using pip") 

check_system.check_filesystem() 


Xshell_runing = True

print("Xshell [Build_ver:"+Welcome.get_ver()+" Running on "+Welcome.get_os_type(),Welcome.get_os_ver()+"]")
print(Welcome.get_welcome_message())
from system.system64 import command
while Xshell_runing == True:
    cwd = os.getcwd()
    print(color('┌──[', fore='blue')+color('Xshell', fore='green')+color(']──[', fore='blue')+cwd+color(']', fore='blue'))

    try:
        user_input = input(color('└─>', fore='blue'))
    except KeyboardInterrupt:
        print(color('\n[!] Keyboard interupt press crtl+c again to exit', fore="yellow"))
        print(color('┌──[', fore='blue')+color('Xshell', fore='green')+color(']──[', fore='blue')+cwd+color(']', fore='blue'))
        try:
            user_input = input(color('└─>', fore='blue'))
        except KeyboardInterrupt:
            exit()

    if "exit" in user_input:
        trim_user_input = user_input[:4]
        if trim_user_input == "exit":
            exit()
    if "quit" in user_input:
        trim_user_input = user_input[:4]
        if trim_user_input == "quit":
            exit()
    command.run(user_input)
    
    
    
