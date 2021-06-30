
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
    def message():
        import datetime
        import socket
        import psutil
        from colr import color
        print(color("Welcome to Xshell "+Welcome.get_ver()+" ("+Welcome.get_os_type()+" "+Welcome.get_os_ver()+")",fore="blue"))
        print()
        print("Source Code: "+ color("https://github.com/awesomelewis2007/Xshell", fore="blue"))
        print("Wiki: "+ color("https://github.com/awesomelewis2007/Xshell/wiki", fore="blue"))
        print("Report Bugs: "+ color("https://github.com/awesomelewis2007/Xshell/issues/new/choose", fore="blue"))
        print("")
        print(color("Version: ",fore="blue")+Welcome.get_ver())
        print(color("Build: ",fore="blue")+Welcome.get_build())
        print(color("Date And Time: ",fore="blue")+str(datetime.datetime.now()))
        print(color("CPU: ",fore="blue")+str(psutil.cpu_percent(interval=0.1))+"%")
        print(color("Local IP Address: ",fore="blue")+socket.gethostbyname(socket.gethostname()))