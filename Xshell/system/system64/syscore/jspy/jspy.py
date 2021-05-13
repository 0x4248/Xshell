import js2py
def run(script):
    js = script
    result = js2py.eval_js(js)
    return result
def run_file(file):
    x = open(file,"r")
    script = x.read()
    js = script
    result = js2py.eval_js(js)
    return result
