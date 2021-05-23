# Xshell
<img src=https://github.com/awesomelewis2007/Xshell/blob/main/document/Xshell_banner.png>
Welcome to the Xshell respitory

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

```
──[Directory]──[~/folder]
[FILE]──[file.txt]
[DIR]──[other_folder]
```
### ls

List the directoy your in but with a more simpler veiw

```
\folder
text.txt
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
```
history
```
### history -c
clears the history 
```
history -c
```
### tree
prints out all the items of your current directory and sub directorys
```
tree
```
