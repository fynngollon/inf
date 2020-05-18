from wuerfel import *
from random import randint
from feld import *
from spielfeld import *
from spieler import *
from figur import *

class Madn(object):
    def __init__(self):
        self.wuerfel = Wuerfel()
        self.spielerliste = []
        for i in range(4):
            self.spielerliste.append(Spieler(i, "Spieler " + str(i)))
        self.spielfeld = Spielfeld(self.spielerliste)

    def makeRandomSituation(self):
        for spieler in self.spielerliste:
            for figur in spieler.figuren:
                feld = self.spielfeld.felderliste[randint(0, len(self.spielfeld.felderliste)-1)]
                if feld.figur == None and (feld.ende == None or feld.ende == spieler):
                    feld.figur = figur
                    figur.setFeld(feld)

    def toXML(self):
        xml = "<madn>" + self.spielfeld.toXML() + "<spielerliste>"
        for spieler in self.spielerliste:
            xml += spieler.toXML()
        xml += "</spielerliste></madn>"

        file = open("text.xml", "a")
        file.write(xml)
        file.close()

        return xml

m = Madn()
