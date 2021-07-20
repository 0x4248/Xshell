def main():
    from system.system64 import lang
    from colr import color
    wm = lang.get_welcome_message()
    print("Your current welcome message is:")
    print(color(wm, fore="blue"))
    ask = input("Do you want to change it (Y) or (N)")
    if ask.upper()[:1] == "Y":
        print("what do you want to change your welcome message to?")
        wm_change = input(color(">",fore="blue"))
        if wm_change == "cancel":
            return None
        try:
            f = open("system/config/welcome/welcome","w")
            f.write(wm_change)
            f.close()
        except:
            print(color("[X] Cant change welcome message", fore="red"))