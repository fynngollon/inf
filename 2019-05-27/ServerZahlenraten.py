import socket
from random import randint

weiter = True
s = socket.socket()
port = 32123
s.bind(('', port))

while weiter:
    s.listen(1)
    (k, adr) = s.accept()
    zufallszahl = randint(1, 100)
    empfangen = k.recv(1024)
    if empfangen < zufallszahl:
        k.send("Groeßer")
    elif empfangen > zufallszahl:
        k.send("Kleiner")
    else:
	k.send("Richtig")
	weiter = False
k.close()
