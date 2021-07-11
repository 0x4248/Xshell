import logging
import os
START_DIR = os.getcwd()
logging.basicConfig(format='[%(asctime)s]  [%(filename)s:%(lineno)d] [ %(levelname)s ]  %(message)s',datefmt='%d-%m-%Y:%H:%M:%S',level=logging.DEBUG,filename='system/temp/logs/System/System_log.log')
global log
log = logging.getLogger(__name__)
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
                error_msg = "CD "+command+" 404"
                log.error(error_msg)
            return None

    if "dir" in command:
        ccommand = command[:3]

        if ccommand == "dir":
            import os
            from colr import color
            dir = os.listdir()
            wd = os.getcwd()
            system_files = [".sys",".cab",".dll",".bin",".reg",".tmp",".temp"]
            executable_files = [".exe",".msi",".sh",".bin"]
            lang_files = [".py",".pyc",".js",".jsm",".c",".h",".hp",".hh",".hpp",".ru",".cs","cpp",".css",".html",".com",".bash",".bat",".java"]
            images = [".png",".jpg",".jpeg",".ico",".webm",".svg",".bmp"]
            data = [".db",".data",".json",".dat",".csv"]
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
            return None

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
            if "-h" in command:
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
            return None
    if "print " in command:
        ccommand = command[:5]
        if ccommand == "print":
            from system.system64.syscom import print as file_print
            file_print.main(command=command)
            return None
    if "$ " in command:
        ccommand = command[:1]
        if ccommand == "$":
            command = command.replace("$","")
            import os
            os.system(command)
        return None
    if "PATH" in command:
        ccommand = command[:4]
        if ccommand == "PATH":
            from system.system64.syscore import PATH
            PATH.main()
        return None

    if "rm " in command:
        from colr import color
        import os
        ccommand = command[:2]
        if ccommand == "rm":
            if "-force" in command:
                command = command.replace("rm ","")  
                command = command.replace(" -force ","") 
                command = command.replace("-force ","") 
                command = command.replace(" -force","") 
                command = command.replace("-force","") 
                try:
                    os.remove(command)
                except FileNotFoundError:
                    from colr import color
                    print(color("[X] File not found 404", fore="red"))
                    error_msg = "GET "+command+" 404"
                    log.error(error_msg)
                except OSError:
                    from colr import color
                    print(color("[X] ERROR OS ERROR 105", fore="red"))
                    error_msg = "SYSTEM OS ERROR Command: "+command
                    log.error(error_msg)  
                return None
            command = command.replace("rm ","")  
            try:
                consent = input(color("[!] Warning the file '"+command+"' Will be removed permanently! \n Are you sure you want to remove this item Y or N:", fore="yellow"))
                consent = consent.capitalize()
                if consent == "Y":
                    os.remove(command)
                if consent != "Y":
                    pass
            except FileNotFoundError:
                from colr import color
                print(color("[X] File not found 404", fore="red"))
                error_msg = "GET "+command+" 404"
                log.error(error_msg)
            except OSError:
                from colr import color
                print(color("[X] ERROR OS ERROR 105", fore="red"))
                error_msg = "SYSTEM OS ERROR Command: "+command
                log.error(error_msg)  
            return None
    if "rmdir " in command:
        from colr import color
        import os
        ccommand = command[:5]
        if ccommand == "rmdir":
            command = command.replace("rmdir ","")  
            try:
                consent = input(color("[!] Warning the directory '"+command+"' Will be removed permanently! \n Are you sure you want to remove this item Y or N:", fore="yellow"))
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
                error_msg = "DIR "+command+" 404"
                log.error(error_msg)
            except OSError:
                from colr import color
                print(color("[X] ERROR OS ERROR 105", fore="red"))
                error_msg = "SYSTEM OS ERROR Command: "+command
                log.error(error_msg) 
            return None
    if "mkdir " in command:
        import os
        ccommand = command[:5]
        if ccommand == "mkdir":
            command = command.replace("mkdir ","")
            try:
                from colr import color
                os.mkdir(command)
                print(color("[+] directory was made 201", fore="green"))
            except FileExistsError:
                from colr import color
                print(color("[!] Warn Directory exists 409", fore="yellow"))
                error_msg = "CREATE EXIST"+command+" 409"
                log.error(error_msg) 
            except OSError:
                from colr import color
                print(color("[X] ERROR OS ERROR 105", fore="red"))
                error_msg = "SYSTEM OS ERROR Command: "+command
                log.error(error_msg) 
            return None
    if "mk " in command:
        ccommand = command[:2]
        if ccommand == "mk":
            command = command.replace("mk ","")
            try:
                x = open(command,"w")
                x.write("")
            except:
                from colr import color
                print(color("[X] Cant write to file 405", fore="red"))
                error_msg = "SYSTEM WRITE FAIL: "+command+" 405"
                log.error(error_msg)
            return None

    if "locip" in command:
        ccommand = command[:5]
        if ccommand == "locip":
            from system.system64.syscore import internet_protocol
            print(internet_protocol.get_local_ip())
            return None

    if "pubip" in command:
        ccommand = command[:5]
        if ccommand == "pubip":
            from system.system64.syscore import internet_protocol
            print(internet_protocol.get_public_ip())
            return None
    if "python " in command:
        ccommand = command[:6]
        if ccommand == "python":
            from system.system64.syscom import py_run
            py_run.main(command=command)
            return None
    if "js " in command:
        ccommand = command[:2]
        if ccommand == "js":
            command = command.replace("js ","")
            from system.system64.syscore.jspy import jspy
            jspy.run_file(command)
            return None
    if "history -c" in command:
        ccommand = command[:10]
        if ccommand == "history -c":
            from system.system64.syscore import history
            history.clear()
            from colr import color
            print(color("Removed all history!", fore="green"))
            log.info("HISTORY CLEARED")
            return None
    if "history -on" in command:
        ccommand = command[:11]
        if ccommand == "history -on":
            from system.system64.syscore import history
            history.set_to("1")
            from colr import color
            print(color("History is now on", fore="green"))
            return None

    if "history -off" in command:
        ccommand = command[:12]
        if ccommand == "history -off":
            from system.system64.syscore import history
            history.set_to("0")
            from colr import color
            print(color("History is now off", fore="green"))
            return None
    if "history" in command:
        ccommand = command[:7]
        if ccommand == "history":
            ccommand = command[7:10]
            from system.system64.syscore import history
            history.read()    
            return None
    if "tree" in command:
        ccommand = command[:4]
        if "--colour-off" in command:
            if ccommand == "tree":
                import os
                path = os.getcwd()
                for root, dirs, files in os.walk(path):
                    level = root.replace(path, '').count(os.sep)
                    indent = ' ' * 4 * (level)
                    print('{}{}/'.format(indent, os.path.basename(root)))
                    subindent = ' ' * 4 * (level + 1)
                    for f in files:
                        print('{}{}'.format(subindent, f))
                return None
        else:
            if ccommand == "tree":
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
            return None

    if "sc" in command:
        if command[:2] == "sc":
            from colr import color
            print("Source Code:", color("https://github.com/awesomelewis2007/Xshell", fore="blue"))
            return None

    if "lines" in command:
        ccommand = command[:5]
        if ccommand == "lines":
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
                error_msg = "GET "+command+" 404"
                log.error(error_msg)
                return None
            return None
    if "tc" in command:
        ccommand = command[:2]
        if ccommand == "tc":
            from colr import color
            import os
            import shutil
            print(color("[!] Warning this will clear all temp including your",fore="yellow")+color("history",fore="red"))
            print("Note: Xshell may not be responsive or crash at any moment if this is done!")
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
    if "wiki" in command:
        if command.upper()[:4] == "WIKI":
            from colr import color
            print("Are you stuck or confused?")
            print("Here is the wiki link: ",color("https://github.com/awesomelewis2007/Xshell/wiki", fore="blue"))
            return None

    if "bug" in command:
        if command.upper()[:3] == "BUG":
            from colr import color
            print("What a bug...")
            print("Here is the issue link:",color("https://github.com/awesomelewis2007/Xshell/issues/new/choose", fore="blue"))
            return None
    if "help" in command:
        if command.upper()[:4] == "HELP":
            if "-l" in command:
                from system.system64.syscore.web.help import help
                help.list()
                return None                
            from system.system64.syscore.web.help import help
            help.main()
            return None
    if "licence" in command:
        if command.upper()[:7] == "LICENCE":
            from system.system64.syscore.web.license import server
            server.main()
            return None
    if "welcome" in command:
        if command[:7] == "welcome":
            from system.system64 import lang
            from colr import color
            wm = lang.get_welcome_message()
            print("Your current welcome message is:")
            print(color(wm, fore="blue"))
            ask = input("Do you want to change it (Y) or (N)")
            if ask.upper()[:1] == "Y":
                print("what do you want to change your welcome message to?")
                wm_change = input(color(">",fore="blue"))
                if wm_change == "cancel":
                    return None
                try:
                    f = open("system/config/welcome/welcome","w")
                    f.write(wm_change)
                    f.close()
                except:
                    print(color("[X] Cant change welcome message", fore="red"))
                return None     
    if "addon_list" in command:
        if command[:10] == "addon_list":
            if "-v" or "-verbose" in command:
                from system.system64.syscore import REGISTRY
                list = REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/ADDONS/INDEX.reg")
                length = len(list)
                list = list[1:length]
                no = 1
                for i in list.splitlines():
                    print(str(no)+"|"+i)
                    no = no + 1
                return None
            from system.system64.syscore import REGISTRY
            list = REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/ADDONS/INDEX.reg")
            list = list.replace(".py","")
            length = len(list)
            print(list[1:length])
            return None
            

    else:
        import difflib
        from colr import color 
        from system.system64 import addon
        command_list = command.split()
        trim = len(str(command_list[:1]).replace("[","").replace("]","").replace("'",""))
        command_replace = command[:trim] + " "
        app = command[:trim]
        trimcommand = command.replace(command_replace,"")
        x = addon.run_addon(name=app,command=trimcommand)
        if x == True:
            return None
        if command == "":
            return None       
        f = open(START_DIR+"/"+"system/REGISTRY/LOCAL_SYSTEM/SYSTEM/SYSTEM_COMMANDS/COMMANDS.data","r")
        x = f.readlines()

        out = difflib.get_close_matches(command,x)
        print(color("Command Not found: "+command, fore="red"))
        
        line= 1
        for i in out:
            i = i.replace("\n", "")
            print(color(line,fore="cyan")+color("> ",fore="blue")+i)
            line = line + 1
