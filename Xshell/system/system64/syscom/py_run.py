def main(command):
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