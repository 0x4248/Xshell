def main(command):
    import logging
    logging.basicConfig(format='[%(asctime)s]  [%(filename)s:%(lineno)d] [ %(levelname)s ]  %(message)s',datefmt='%d-%m-%Y:%H:%M:%S',level=logging.DEBUG,filename='system/temp/logs/System/System_log.log')
    global log
    log = logging.getLogger(__name__)
    command = command.replace("print ","")
    try:
        file = open(command,"r")
        print(file.read()) 
        return None   
    except FileNotFoundError: 
        from colr import color
        print(color("[X] File not found 404", fore="red"))
        error_msg = "GET "+command+" 404"
        log.error(error_msg)