import socket

while True:
    s = socket.socket()
    port = 32123
    s.bind(('', port))
    s.listen(1)
    (k, adr) = s.accept()
    empfangen = k.recv(1024)
    k.send(empfangen)
    k.close()
