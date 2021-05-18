def read():
    f = open("system/temp/history","r")
    x = f.read()
    x = x.replace("{Xshell - History}","")
    print(x)

def clear():
    f = open("system/temp/history","w")
    f.write("{Xshell - History}")

def write(command):
    f = open("system/temp/history","a")
    f.write("\n"+command)