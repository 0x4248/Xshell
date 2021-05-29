#Xshell
global LOG_STATE
LOG_STATE = 1
class Boot:
    def Fatal_cant_boot(errorno = "Unknown error no",reason = "No reason was given",log = "No log file was found",fix = "No fixes available"):
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
                log = log + "Xshell Will Not contine to boot"+"\n"
                log = log + "Printing error message and quitting"
                a = "CHECK DISK: The system cant find the path '"+i+"'"
                Boot.Fatal_cant_boot(errorno="404",reason=a,log=log,fix="Reinstall Xshell or relocate the missing path or file")
    def Host_info():
        if LOG_STATE == 1:
            from system.system64.syscore import REGISTRY
            x = platform.system()
            x = x.upper()
            REGISTRY.write("system/REGISTRY/LOCAL_MACHINE/LOCAL_OS/system_os.data",x)
            REGISTRY.write("system/temp/OS",x)

            x = platform.version()
            REGISTRY.write("system/REGISTRY/LOCAL_MACHINE/LOCAL_NAME/NAME.data",x)
            REGISTRY.write("system/temp/OS_NAME",x)
        if LOG_STATE == 0:
            pass


    def path_add():
        import sys
        import os
        paths = ["system/temp","system"]
        for p in paths:
            sys.path.append(p)
        cwd = os.getcwd()
        sys.path.append(cwd)
    def check_modules():
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
            import js2py
        except:
            Boot.Fatal_cant_boot(errorno="403",reason="Xshell can't import the module js2py",log="none",fix="try to install the module using pip")
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
class Welcome:
    def get_welcome_message():
        from system.system64 import lang
        return lang.get_welcome_message()

    def get_ver():
        from system.system64 import lang
        ver = lang.get_sys_ver()
        ver = str(ver)
        return ver

    def get_build():
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

#=====================MAIN======================

Boot.check_modules()
Boot.path_add()
Boot.check_filesystem()
import os
import sys
import time
import js2py
import datetime
import platform
from colr import color
import requests
import socket

Boot.Host_info()

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
#====Welcome===
print("Xshell [SYS_VER: "+color(Welcome.get_ver(), fore="blue")+"] [BUILD_VER: "+color(Welcome.get_build(), fore="blue")+"] [SYSTEM: "+Welcome.get_os_type(),Welcome.get_os_ver()+"]")
if LOG_STATE == 0:
    print(color("Xshell has started in no REG logging mode",fore="yellow"))
#===SYSTEM IMPORT===
from system.system64 import command
from system.system64.syscore import history
from system.system64.syscore import REGISTRY
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