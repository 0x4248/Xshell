def test_command_1():
    from system.system64 import command
    command.run("makefile test.txt")
def test_command_2():
    from system.system64 import command
    command.run("ls")
def test_command_3():
    from system.system64 import command
    command.run("tree")
def test_command_4():
    from system.system64 import command
    command.run("history")
def test_command_5():
    from system.system64 import command
    command.run("history -c")
def test_language_1():
    from system.system64 import lang
    lang.get_lang()
def test_language_2():
    from system.system64 import lang
    lang.get_welcome_message()

    
