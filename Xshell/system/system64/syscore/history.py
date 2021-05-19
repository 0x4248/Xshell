import os
wd = os.getcwd()
def read():  
    f = open(wd+"/"+"system/temp/history","r")
    x = f.read()
    x = x.replace("{Xshell - History}","")
    print(x)

def clear():
    f = open(wd+"/"+"system/temp/history","w")
    f.write("{Xshell - History}")

def write(command):
    f = open(wd+"/"+"system/temp/history","a")
    f.write("\n"+command)