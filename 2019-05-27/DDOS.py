import socket

def client():
    while True:
        c=socket.socket()
        port=11112
        ip="192.168.1.157"
        c.connect((ip,port))
        text = "B"
        c.send(bytes(text,"ascii"))
        c.close()
