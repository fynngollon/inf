import socket

while True:
    c = socket.socket()
    ip = input("Type in an IP-Adress: ")
    port = input("Type in a port: ")
    c.connect((ip, int(port)))
    empfangen = ""
    while empfangen != "Richtig":
        msg = input("Rate eine Zahl: ")
        c.send(bytes(msg, 'ascii'))
        empfangen = c.recv(1024)
        print(empfangen)
    c.close
