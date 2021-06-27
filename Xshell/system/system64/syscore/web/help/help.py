def main():
    import urllib.request
    contents = urllib.request.urlopen("https://raw.githubusercontent.com/wiki/awesomelewis2007/Xshell/Commands.md").read()
    doc = contents.decode("utf-8")
    doc = doc.replace("#","")
    doc = doc.replace("`","")
    doc = doc.replace('b"',"")
    doc = doc.replace('" ',"")
    print(doc)