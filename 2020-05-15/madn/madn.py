from tkinter.filedialog import asksaveasfile, askopenfile
from xml.dom.minidom import *
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
        xml = "<madn>"
        for i in self.spielerliste:
            xml += i.toXML()
        xml += "</spielerliste></madn>"
        f = asksaveasfile(mode="w", defaultextension=".madn", filetypes=[("MADN", ".madn")])
        f.write(xml)
        f.close()
        return xml

    def fromXML(self):
        f = askopenfile(mode="r", filetypes=[("MADN", ".madn")])
        xml = f.read()
        f.close()
        document = parseString(xml)
        madn = document.firstChild
        self.spielerliste = []
        spielerliste = madn.getElementsByTagName('spielerliste')[0]
        spieler = spielerliste.getElementsByTagName('spieler')



m = Madn()
