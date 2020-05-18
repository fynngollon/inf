import socket

while True:
    c = socket.socket()
    ip = input("An wen soll die nachricht gehen?:")
    port = input("Welcher Port wird verwendet?:")
    c.connect((ip, int(port)))
    empfangen = "a"
    while empfangen != "Richtig":
        msg = input("Was glaubst du ist Richtig?:")
        c.send(bytes(msg,'ascii'))
        empfangen = c.recv(1024)
        print(empfangen)
    c.close
       
