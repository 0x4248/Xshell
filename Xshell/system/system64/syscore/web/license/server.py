def main():
    import webbrowser
    import os
    from system.system64.syscore import REGISTRY

    webbrowser.open_new_tab(REGISTRY.read("system/REGISTRY/LOCAL_SYSTEM/PATH/START_DIR/START_DIR.reg")+"/system/system64/syscore/web/license/index.html")