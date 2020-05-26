from wuerfel import *
from random import randint
from feld import *
from spielfeld import *
from spieler import *
from figur import *
from tkinter.filedialog import asksaveasfile, askopenfile
from xml.dom.minidom import *

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
                feld = self.spielfeld.felderliste[randint(
                    0, len(self.spielfeld.felderliste)-1)]
                if feld.figur == None and (feld.ende == None or feld.ende == spieler):
                    feld.figur = figur
                    figur.setFeld(feld)

    def toXML(self):
        xml = "<madn>"
        xml += "<spielerliste>"
        for spieler in self.spielerliste:
            xml += spieler.toXML()
        xml += "</spielerliste>"
        xml += "</madn>"
        f = asksaveasfile(mode="w", defaultextension='.madn', filetypes=[('MADN', '.madn')])
        f.write(xml)
        f.close()

    def fromXML(self):
        f = askopenfile(mode="r", filetypes=[('MADN', '.madn')])
        xml = f.read()
        f.close()
        document = parseString(xml)
        madn = document.firstChild
        self.spielerliste = []
        spielerliste = madn.getElementsByTagName('spielerliste')[0]
        #laden der Spieler
        spieler = spielerliste.getElementsByTagName('spieler')
        for s in spieler:
            if s.getElementsByTagName('farbe')[0].firstChild != None :
                self.spielerliste.append(Spieler(int(s.getAttribute('id')), s.getElementsByTagName('name')[0].firstChild.nodeValue, s.getElementsByTagName('farbe')[0].firstChild.nodeValue ))
            else:
                self.spielerliste.append(Spieler(int(s.getAttribute('id')), s.getElementsByTagName('name')[0].firstChild.nodeValue))
        #erzeugen des Spielfelds
        self.spielfeld = Spielfeld(self.spielerliste)

        #Positionieren der Figuren
        zaehler = 0
        for s in spieler:
            figurenliste = s.getElementsByTagName('figurenliste')[0]
            self.spielerliste[zaehler].fromXML(figurenliste, self.spielfeld)
            zaehler += 1

m = Madn()
        










