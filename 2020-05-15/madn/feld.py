class Feld(object):
    def __init__(self, fid,  anfang=None, ende=None):
        self.id = fid #bekommt eine id
        self.figur = None
        self.nachfolger = []
        self.anfang = anfang #Falls es ein Startfeld ist
        self.ende = ende #Falls es ein Endefeld ist

    def addNachfolger(self, nachfolger):
        #Fügt ein Feld hinzu, dass nach diesem Feld kommt
        self.nachfolger.append(nachfolger)

    def setAnfang(self, spieler):
        #Setzt den Spieler fest, dem dieses Feld als Start dient
        self.anfang = spieler

    def setEnde(self, spieler):
        #Setzt den Spieler fest, dem dieses Feld als Ende dient
        self.ende = spieler

    def toXML(self):
        xml = '<feld id="' + str(self.id) + '">'
        if self.anfang != None:
            xml += "<start>" + str(self.anfang.id) + "</start>"
        if self.ende != None:
            xml += "<ende>" + str(self.ende.id) + "</ende>"
        xml += "<naechste>"
        for nachfolger in self.nachfolger:
            xml += "<feldid>" + str(nachfolger.id) + "</feldid>"
        xml += "</naechste></feld>"
        return xml
