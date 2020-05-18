import socket
from random import randint

s = socket.socket()
port = 32125
s.bind(('', port))
antwort = ""
zufallszahl = 0
empfangen = 101
anfang = True
s.listen(1)
(k, adr) = s.accept()

while empfangen != zufallszahl:
    if anfang:
        zufallszahl = randint(0,100)
        anfang = False
    
    empfangen = int(k.recv(1024))
    if zufallszahl > empfangen:
        antwort = "zu niedrig"
    elif zufallszahl < empfangen:
        antwort = "zu hoch"
    else:
        antwort = "Richtig"
    k.send(bytes(antwort,'ascii'))
    
k.close()
antwort = ""
anfang = True
empfangen = 101
