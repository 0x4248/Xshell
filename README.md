<h1>Welcome to the Xshell Source Code</h1>
<img src=https://github.com/awesomelewis2007/Xshell/blob/main/document/Xshell_banner.png>

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/awesomelewis2007/Xshell?label=Xshell)
![GitHub](https://img.shields.io/github/license/awesomelewis2007/Xshell?color=blue)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/awesomelewis2007/Xshell?label=Latest%20version%20%20)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/awesomelewis2007/Xshell?color=blue&include_prereleases)
![Pyver](https://img.shields.io/badge/Python%20Version-3.9.5-blue)
![GitHub top language](https://img.shields.io/github/languages/top/awesomelewis2007/Xshell)

Xshell is a simple python shell that runs in a local folder

<img src=https://github.com/awesomelewis2007/Xshell/blob/main/document/screenshots/Screenshot_of_shell.png>

## Installing

to install Xshell and its depencancies you need to run the installer

### using python

on linux

```
cd Xshell_installer
python3 install.py
```
on win
```
cd Xshell_installer
python install.py
```
### using bash (linux with bash)

```
cd Xshell_installer
bash install.bash
```
### using cmd (windows)

```
cd Xshell_installer
install.cmd
```

## Commands

### cd

Change directory
This command is used for changing the directory

If i am in a folder called folder 1 and i need to get to folder 2

You put into the shell `cd folder 2 `

You can also do `cd \` to go to your root folder

### dir

This lists the directoy that your currently in like
-c   --colour      prints files with colouring
-h   --help        prints this help message
```
dir [-c,-h]
```
### ls

List the directoy your in but with a more simpler veiw
-c   --colour      prints files with colouring
-d   --directory   only prints directory's
-f   --files       only prints files
-h   --help        prints this help message
```
ls [-d,-h,-f,-c]
```

Note files will be coloerd white and directorys will be blue

### print 
Prints a file onto the terminal
```
print <file name>
```

### $
This command lets the shell run a command to the os

```
$ <command>
```

### rm
Removes a file of the disk perminently
```
rm <file name>
```

### rmdir
Removes a directory and what it conatins
```
rmdir <dir>
```

### mkdir
Creates a directory
```
mkdir <name>
```
### makefile
Create a file
```
makefile <file name>
```


### locip
Returns the local ip address
```
locip
```

### pubip
Returns the public ip address
```
pubip
```

### python
runs a python script
```
python <file name>
```

### js
runs a js file using js2py
```
js <file name>
```

### history
reads the history and prints it on the screen

the argument `-c` clears the history
the argument `-on` turn on history logging
the argument `-c` turn off history logging
```
history [-c,-on,-off]
```

### tree
prints out all the items of your current directory and sub directorys
the argument `--colour-off` prints without colouring
```
tree[--colour-off]
```
