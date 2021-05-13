import js2py
def run(script):
    js = script
    result = js2py.eval_js(js)
    return result
