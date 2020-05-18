from figur import *
class Spieler(object):
    def __init__(self, sid, name, farbe=""):
        self.id = sid #id und Name hinzugefügt
        self.name = name
        self.farbe = farbe
        self.figuren = []   #leere Figurenliste
        for i in range(4):  #4 Figuren für den Spieler erzeugen
            self.figuren.append(Figur(self))

    def toXML(self):
        xml = '<spieler id="' + str(self.id) + '">'
        xml += '<name>' + self.name + '</name>'
        xml += '<farbe>' + self.farbe + '</farbe>'
        xml += '<figurenliste>'
        for figur in self.figuren:
            xml += figur.toXML()
        xml += "</figurenliste></spieler>"

        return xml
