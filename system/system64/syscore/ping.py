from re import A


def ping(v=False,a=1,t=""):
    """[summary]

    Args:
        v (bool, optional): [verbose]. Defaults to False.
        a (int, optional): [amount]. Defaults to 1.
        t (str, optional): [target]. Defaults to "".
    """
    if t == "":
        from colr import color
        print(color("[X] Please enter a domain"))
        return "ERROR"
    import pythonping
    return pythonping.ping(t,verbose=v,count=a)
    
