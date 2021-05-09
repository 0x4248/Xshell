def get_local_ip():
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_public_ip():
    import requests
    return requests.get('https://api.ipify.org').text
