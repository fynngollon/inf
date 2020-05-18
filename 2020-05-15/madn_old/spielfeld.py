from feld import *

class Spielfeld(object):
    def __init__(self, spielerliste):
        self.felderliste = [] #leere Liste in die später alle Felder abgespeichert werden

        for i in range(40): #Erzeuge 40 Felder für alle Felder zum Herumlaufen
            feld = Feld(i) #Erzeuge ein Feld mit der ID i
            if i != 0:  
                self.felderliste[-1].addNachfolger(feld) #Füge Feld dem letzten Feld in der Liste als Nachfolger hinzu
            self.felderliste.append(feld)
        self.felderliste[-1].addNachfolger(self.felderliste[0])

        for i in range(4):
            feld = self.felderliste[i*10]
            feld.setAnfang(spielerliste[i])#lege die 4 Anfangsfelder fest für jeden Spieler

            feld = self.felderliste[-1+i*10]
            for j in range(4):#Erzeuge das Haus des Spielers
                feldNeu = Feld(40 + i*4 + j, ende=spielerliste[i])
                feld.addNachfolger(feldNeu)
                feld = feldNeu
                self.felderliste.append(feld)

            
