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
    def Host_info():
        x = platform.system()
        x = x.upper()
        f = open("system/REGISTRY/LOCAL_MACHINE/LOCAL_OS/system_os.data","w")
        f.write(x)
        f.close()
        f = open("system/temp/OS","w")
        f.write(x)
        f.close()

        x = platform.version()
        f = open("system/REGISTRY/LOCAL_MACHINE/LOCAL_NAME/NAME.data","w")
        f.write(x)
        f.close()
        f = open("system/temp/OS_NAME","w")
        f.write(x)
        f.close()

    def path_add():
        import sys
        import os
        paths = ["system/temp","system"]
        for p in paths:
            sys.path.append(p)
        cwd = os.getcwd()
        sys.path.append(cwd)

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
        paths = ["system","system/system64","system/system64/syscore"]
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
    import requests
except:
    Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module requests",log="none",fix="try to install the module using pip") 
try:
    import socket
except:
    Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module socket",log="none",fix="try to install the module using pip") 
try:
    import pythonping
except:
    Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module pythonping",log="none",fix="try to install the module using pip") 

Boot.path_add()
check_system.check_filesystem() 


#Boot.Host_info()

#====History====
Xshell_runing = True
try:
    history_file_read = open("system/temp/history","r")
    history_file_read_x = history_file_read.read()
except:
    history_file_read = open("system/temp/history","w")
    history_file_read.close()
    history_file_read = open("system/temp/history","r")
    history_file_read_x = history_file_read.read()
#====Welcome====
print("Xshell [Build_ver:"+Welcome.get_ver()+" Running on "+Welcome.get_os_type(),Welcome.get_os_ver()+"]")
print(Welcome.get_welcome_message())

#===SYSTEM IMPORT===
from system.system64 import command
from system.system64.syscore import history
#===SYS LOOP===
while Xshell_runing == True:
    cwd = os.getcwd()
    xshell_text = "Xshell@"+socket.gethostname()
    print(color('┌──[', fore='blue')+color(xshell_text, fore='green')+color(']──[', fore='blue')+cwd+color(']', fore='blue'))
    try:
        user_input = input(color('└─>', fore='blue'))
        history.write(user_input)
    except KeyboardInterrupt:
        print(color('\n[!] Keyboard interupt press crtl+c again to exit', fore="yellow"))
        print(color('┌──[', fore='blue')+color(xshell_text, fore='green')+color(']──[', fore='blue')+cwd+color(']', fore='blue'))
        try:
            user_input = input(color('└─>', fore='blue'))
        except KeyboardInterrupt:
            print("\n")
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