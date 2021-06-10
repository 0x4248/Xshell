import logging
logging.basicConfig(format='[%(asctime)s]  [%(filename)s:%(lineno)d] [ %(levelname)s ]  %(message)s',datefmt='%d-%m-%Y:%H:%M:%S',level=logging.DEBUG,filename='system/temp/logs/System/System_log.log')
global log
log = logging.getLogger('Command')

def run(command):
    if "cd " in command:
        ccommand = command[:2]
        if ccommand == "cd":
            command = command.replace("cd ","")
            import os 
            try:
                os.chdir(command)
            except FileNotFoundError:
                from colr import color
                print(color("[X] Directory not found 404", fore="red"))

    if "dir" in command:
        ccommand = command[:3]

        if ccommand == "dir":
            import os
            from colr import color
            dir = os.listdir()
            wd = os.getcwd()
            system_files = [".sys",".cab",".dll",".bin",".reg",".tmp",".temp"]
            executable_files = [".exe",".msi",".sh"]
            lang_files = [".py",".pyc",".js",".jsm",".c",".h",".cs","cpp",".css",".html",".com",".bash",".bat",".java"]
            images = [".png",".jpg",".jpeg",".ico"]
            data = [".db",".data",".json",".dat"]
            if "-c" in command:
                from random import randint
                if randint(1,1000) == 1:
                    x = ["[","D","i","r","n","e","c","t","o","r","y","]","─","─","[",wd,"]"]
                    print(color("[",fore="green")+color("D",fore="blue")+color("i",fore="red")+color("r",fore="green")+
                    color("e",fore="blue")+color("c",fore="red")+color("t",fore="green")+color("o",fore="blue")+
                    color("r",fore="red")+color("y",fore="green")+color("]",fore="blue")+color("─",fore="red")+
                    color("─",fore="green")+color("[",fore="blue")+color(wd,fore="red")+color("]",fore="green"))
                print("[Directory]──["+wd+"]")
                for i in dir:
                    full_dir = wd+"/"+i
                    if os.path.isfile(full_dir) == True:
                        for file in system_files:
                            if i.endswith(file) == True:
                                print(color(i,fore="blue"))
                        for file in executable_files:
                            if i.endswith(file) == True:
                                print(color(i,fore="green"))
                        for file in lang_files:
                            if i.endswith(file) == True:
                                print(color(i,fore="cyan"))
                        for file in images:
                            if i.endswith(file) == True:
                                print(color(i,fore="orange"))
                        for file in data:
                            if i.endswith(file) == True:
                                print(color(i,fore="purple"))
                    if os.path.isdir(full_dir) == True:
                        print("/"+i)
                return None
            if "--colour" in command:
                from random import randint
                if randint(1,1000) == 1:
                    x = ["[","D","i","r","n","e","c","t","o","r","y","]","─","─","[",wd,"]"]
                    print(color("[",fore="green")+color("D",fore="blue")+color("i",fore="red")+color("r",fore="green")+
                    color("e",fore="blue")+color("c",fore="red")+color("t",fore="green")+color("o",fore="blue")+
                    color("r",fore="red")+color("y",fore="green")+color("]",fore="blue")+color("─",fore="red")+
                    color("─",fore="green")+color("[",fore="blue")+color(wd,fore="red")+color("]",fore="green"))
                print("[Directory]──["+wd+"]")
                for i in dir:
                    full_dir = wd+"/"+i
                    if os.path.isfile(full_dir) == True:
                        for file in system_files:
                            if i.endswith(file) == True:
                                print(color(i,fore="blue"))
                        for file in executable_files:
                            if i.endswith(file) == True:
                                print(color(i,fore="green"))
                        for file in lang_files:
                            if i.endswith(file) == True:
                                print(color(i,fore="cyan"))
                        for file in images:
                            if i.endswith(file) == True:
                                print(color(i,fore="orange"))
                        for file in data:
                            if i.endswith(file) == True:
                                print(color(i,fore="purple"))
                    if os.path.isdir(full_dir) == True:
                        print("/"+i)
                return None
            if "--help" in command:
                print("Usage of dir command")
                print("dir [-command]")
                print("-c   --colour      prints files with colouring")
                print("-h   --help        prints this help message")
                return None
            if "--help" in command:
                print("Usage of dir command")
                print("dir [-command]")
                print("-c   --colour      prints files with colouring")
                print("-h   --help        prints this help message")
                return None
            print("[Directory]──["+wd+"]")
            for i in dir:
                full_dir = wd+"/"+i
                if os.path.isfile(full_dir) == True:
                    print("[FILE]─["+i+"]")
                if os.path.isdir(full_dir) == True:
                    print("[DIR]──["+i+"]")

    if "ls" in command:
        from colr import color
        ccommand = command[:2]
        if ccommand == "ls":
            import os
            dir = os.listdir()
            wd = os.getcwd()
            #file colouring
            system_files = [".sys",".cab",".dll",".bin",".reg",".tmp",".temp"]
            executable_files = [".exe",".msi",".sh"]
            lang_files = [".py",".pyc",".js",".jsm",".c",".h",".cs","cpp",".css",".html",".com",".bash",".bat",".java"]
            images = [".png",".jpg",".jpeg",".ico"]
            data = [".db",".data",".json",".dat"]
            if "-d" in command:
                for i in dir:
                    full_dir = wd+"/"+i
                    if os.path.isfile(full_dir) == True:
                        pass
                    if os.path.isdir(full_dir) == True:
                        print("/"+i)
                return None
            if "--directory" in command:
                for i in dir:
                    full_dir = wd+"/"+i
                    if os.path.isfile(full_dir) == True:
                        pass
                    if os.path.isdir(full_dir) == True:
                        print("/"+i)
                return None
            if "-f" in command:
                for i in dir:
                    full_dir = wd+"/"+i
                    if os.path.isfile(full_dir) == True:
                        print(color(i,fore="white"))
                    if os.path.isdir(full_dir) == True:
                        pass
                return None

            if "--files" in command:
                for i in dir:
                    full_dir = wd+"/"+i
                    if os.path.isfile(full_dir) == True:
                        print(color(i,fore="white"))
                    if os.path.isdir(full_dir) == True:
                        pass
                return None

            if "-c" in command:
                for i in dir:
                    full_dir = wd+"/"+i
                    if os.path.isfile(full_dir) == True:
                        for file in system_files:
                            if i.endswith(file) == True:
                                print(color(i,fore="blue"))
                        for file in executable_files:
                            if i.endswith(file) == True:
                                print(color(i,fore="green"))
                        for file in lang_files:
                            if i.endswith(file) == True:
                                print(color(i,fore="cyan"))
                        for file in images:
                            if i.endswith(file) == True:
                                print(color(i,fore="orange"))
                        for file in data:
                            if i.endswith(file) == True:
                                print(color(i,fore="purple"))
                    if os.path.isdir(full_dir) == True:
                        print("/"+i)
                return None
            if "--colour" in command:
                for i in dir:
                    full_dir = wd+"/"+i
                    if os.path.isfile(full_dir) == True:
                        for file in system_files:
                            if i.endswith(file) == True:
                                print(color(i,fore="blue"))
                        for file in executable_files:
                            if i.endswith(file) == True:
                                print(color(i,fore="green"))
                        for file in lang_files:
                            if i.endswith(file) == True:
                                print(color(i,fore="cyan"))
                        for file in images:
                            if i.endswith(file) == True:
                                print(color(i,fore="orange"))
                        for file in data:
                            if i.endswith(file) == True:
                                print(color(i,fore="purple"))
                    if os.path.isdir(full_dir) == True:
                        print("/"+i)
                return None
            if "--help" in command:
                print("Usage of ls command")
                print("ls [-command]")
                print("-c   --colour      prints files with colouring")
                print("-d   --directory   only prints directory's")
                print("-f   --files       only prints files")
                print("-h   --help        prints this help message")
                return None
            if "--help" in command:
                print("Usage of ls command")
                print("ls [-command]")
                print("-c   --colour      prints files with colouring")
                print("-d   --directory   only prints directory's")
                print("-f   --files       only prints files")
                print("-h   --help        prints this help message")
                return None
            for i in dir:
                full_dir = wd+"/"+i
                if os.path.isfile(full_dir) == True:
                    print(color(i,fore="white"))
                if os.path.isdir(full_dir) == True:
                    print(color(i,fore="white"))

    if "print " in command:
        ccommand = command[:5]
        if ccommand == "print":
            command = command.replace("print ","")
            try:
                file = open(command,"r")
                print(file.read())    
            except FileNotFoundError:
                from colr import color
                print(color("[X] File not found 404", fore="red"))
    if "$ " in command:
        ccommand = command[:1]
        if ccommand == "$":
            command = command.replace("$","")
            import os
            os.system(command)

    if "PATH" in command:
        ccommand = command[:4]
        if ccommand == "PATH":
            from system.system64.syscore import PATH
            PATH.main()

    if "rm " in command:
        from colr import color
        import os
        ccommand = command[:2]
        if ccommand == "rm":
            command = command.replace("rm ","")  
            try:
                consent = input(color("[!] Are you sure you want to remove this file Y or N:", fore="yellow"))
                consent = consent.capitalize()
                if consent == "Y":
                    os.remove(command)
                if consent != "Y":
                    pass
            except FileNotFoundError:
                from colr import color
                print(color("[X] Warn File not found 404", fore="red"))
            except OSError:
                from colr import color
                print(color("[X] ERROR OS ERROR 105", fore="red"))

    if "rmdir " in command:
        from colr import color
        import os
        ccommand = command[:5]
        if ccommand == "rmdir":
            command = command.replace("rmdir ","")  
            try:
                consent = input(color("[!] Are you sure you want to remove this directory Y or N:", fore="yellow"))
                consent = consent.capitalize()
                if consent == "Y":
                    x = os.getcwd()
                    command = x + "/" + command
                    os.rmdir(command)
                if consent != "Y":
                    pass
            except FileNotFoundError:
                from colr import color
                print(color("[X] Warn directory not found 404", fore="red"))
            except OSError:
                from colr import color
                print(color("[X] ERROR OS ERROR 105", fore="red"))


    if "mkdir " in command:
        import os
        ccomand = command[:5]
        if ccomand == "mkdir":
            command = command.replace("mkdir ","")
            try:
                from colr import color
                os.mkdir(command)
                print(color("[+] directory was made 201", fore="green"))
            except FileExistsError:
                from colr import color
                print(color("[!] Warn Directory exists 409", fore="yellow"))
            except OSError:
                from colr import color
                print(color("[X] ERROR OS ERROR 105", fore="red"))

    if "makefile " in command:
        ccomand = command[:8]
        if ccomand == "makefile":
            command = command.replace("makefile ","")
            try:
                x = open(command,"w")
                x.write("")
            except:
                from colr import color
                print(color("[X] Cant write to file 404", fore="red"))

    if "locip" in command:
        ccomand = command[:5]
        if ccomand == "locip":
            from system.system64.syscore import internet_protocol
            print(internet_protocol.get_local_ip())
            

    if "pubip" in command:
        ccomand = command[:5]
        if ccomand == "pubip":
            from system.system64.syscore import internet_protocol
            print(internet_protocol.get_public_ip())

    if "python " in command:
        ccomand = command[:6]
        if ccomand == "python":
            command = command.replace("python ","")
            import platform
            import os
            s = platform.system()
            s = s.upper()
            if s == "LINUX":
                x = "python3 "+command
                os.system(x)

            if s == "MACOS":
                x = "python3 "+command
                os.system(x)
            
            if s == "WINDOWS":
                x = "python "+command
                os.system(x)
    if "js " in command:
        ccomand = command[:2]
        if ccomand == "js":
            command = command.replace("js ","")
            from system.system64.syscore.jspy import jspy
            jspy.run_file(command)
    if "history -c" in command:
        ccomand = command[:10]
        if ccomand == "history -c":
            from system.system64.syscore import history
            history.clear()
            from colr import color
            print(color("Removed all history!", fore="green"))

    if "history -on" in command:
        ccomand = command[:11]
        if ccomand == "history -on":
            from system.system64.syscore import history
            history.set_to("1")
            from colr import color
            print(color("History is now on", fore="green"))

    if "history -off" in command:
        ccomand = command[:12]
        if ccomand == "history -off":
            from system.system64.syscore import history
            history.set_to("0")
            from colr import color
            print(color("History is now off", fore="green"))

    if "history" in command:
        ccomand = command[:7]
        if ccomand == "history":
            ccomand = command[7:10]
            from system.system64.syscore import history
            history.read()    

    if "tree" in command:
        ccomand = command[:4]
        if "--colour-off" in command:
            if ccomand == "tree":
                import os
                path = os.getcwd()
                for root, dirs, files in os.walk(path):
                    level = root.replace(path, '').count(os.sep)
                    indent = ' ' * 4 * (level)
                    print('{}{}/'.format(indent, os.path.basename(root)))
                    subindent = ' ' * 4 * (level + 1)
                    for f in files:
                        print('{}{}'.format(subindent, f))
        if "--colour-off" not in command:
            if ccomand == "tree":
                import os
                from colr import color
                path = os.getcwd()
                for root, dirs, files in os.walk(path):
                    level = root.replace(path, '').count(os.sep)
                    indent = ' ' * 4 * (level)
                    print(color('{}{}/'.format(indent, os.path.basename(root)), fore="blue"))
                    subindent = ' ' * 4 * (level + 1)
                    for f in files:
                        print('{}{}'.format(subindent, f))
    if "github" in command:
        from colr import color
        print("Source Code:", color("https://github.com/awesomelewis2007/Xshell", fore="blue"))
    
    if "lines" in command:
        ccomand = command[:5]
        if ccomand == "lines":
            command = command.replace("lines ","")
            count=0
            try:
                with open(command) as f:
                    for _ in f:
                        count += 1
                        print(count)
            except FileNotFoundError:
                from colr import color
                print(color("[X] File no found 404", fore="red"))
                return None
    if "fc" in command:
        ccomand = command[:2]
        if "-t" in command:
            from colr import color
            import os
            import shutil
            
            print(color("[!] Warning this will clear all temp including your",fore="yellow")+color("history",fore="red"))
            print("Note: Xshell may not be responsive or crash at any moment if this is done!")
            dir = os.listdir("system/temp")

            for i in dir:
                path = "system/temp"+"/"+str(i)
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