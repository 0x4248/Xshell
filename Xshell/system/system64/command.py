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
            dir = os.listdir()
            wd = os.getcwd()
            print("[Directory]──["+wd+"]")
            for i in dir:
                full_dir = wd+"/"+i
                if os.path.isfile(full_dir) == True:
                    print("[FILE]─["+i+"]")
                if os.path.isdir(full_dir) == True:
                    print("[DIR]──["+i+"]")
    if "ls" in command:
        from colr import color
        ccommand = command[:3]
        if ccommand == "ls":
            import os
            dir = os.listdir()
            wd = os.getcwd()
            for i in dir:
                full_dir = wd+"/"+i
                if os.path.isfile(full_dir) == True:
                    print(color(i, fore="white"))
                if os.path.isdir(full_dir) == True:
                    xi = "/"+i+""
                    print(color(xi, fore="blue"))
    
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
            x = open(command,"w")
            x.write("")

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
            s = platform.system()
            s = s.upper()
            if s == "LINUX":
                x = "python3",command
                os.system(x)

            if s == "MACOS":
                x = "python3",command
                os.system(x)
            
            if s == "WINDOWS":
                x = "python",command
                os.system(x)
    if "js " in command:
        ccomand = command[:2]
        if ccomand == "js":
            command = command.replace("js ","")
            from system.system64.syscore.jspy import jspy
            jspy.run_file(command)
    if "history" in command:
        ccomand = command[:7]
        if ccomand == "history":
            ccomand = command[7:10]
            if ccomand != " -c":
                from system.system64.syscore import history
                history.read()            
    if "history -c" in command:
        ccomand = command[:10]
        if ccomand == "history -c":
            from system.system64.syscore import history
            history.clear()
