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
        print("Welcome to Xshell "+Welcome.get_ver()+" ("+Welcome.get_os_type()+" "+Welcome.get_os_ver()+")")
        print()
        print("Source Code: https://github.com/awesomelewis2007/Xshell")
        print("Wiki: https://github.com/awesomelewis2007/Xshell/wiki")
        print("Report Bugs: https://github.com/awesomelewis2007/Xshell/issues/new/choose")
        print("")
        print("Date: ",datetime.datetime.now())
        print("CPU: "+str(psutil.cpu_percent(interval=0.1))+"%")
        print("Local IP Address: "+socket.gethostbyname(socket.gethostname()))
        print("")
