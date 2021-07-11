def main():
    import urllib.request
    from colr import color
    contents = urllib.request.urlopen("https://raw.githubusercontent.com/wiki/awesomelewis2007/Xshell/Commands.md").read()
    doc = contents.decode("utf-8")
    doc = doc.replace("# ","")
    doc = doc.replace("`","")
    doc = doc.replace('b"',"")
    doc = doc.replace('" ',"")
    print("Help from https://github.com/awesomelewis2007/Xshell/wiki/Commands")
    print(color("[!] Some commands in this help list may not work becuse this may be a newer documentation"))
    print(doc)
def list():
    from system.system64.syscore import REGISTRY
    print("Installed commands (Not addons):")
    print(REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/SYSTEM/SYSTEM_COMMANDS/COMMANDS.data"))