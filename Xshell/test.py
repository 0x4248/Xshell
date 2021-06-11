def test_1():
    from system.system64 import command
    command.run("dir")
def test_2():
    from system.system64 import command
    command.run("ls")
def test_3():
    from system.system64 import command
    command.run("tree")
def test_4():
    from system.system64 import command
    command.run("history")
def test_5():
    from system.system64 import command
    command.run("history -c")
def test_6():
    from system.system64 import lang
    lang.get_lang()
def test_7():
    from system.system64 import lang
    lang.get_welcome_message()
def test_8():
    import main
    