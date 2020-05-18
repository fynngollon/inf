class Figur(object):
    def __init__(self, spieler):
        self.spieler = spieler #bekommt einen Spieler zugeordnet
        self.feld = None

    def setFeld(self, feld):
        self.feld = feld # bekommt tatsächlich ein Feld
    
    def toXML(self):
        xml = "<figur>"
        if self.feld != None:
            xml += "<feldid>" + str(self.feld.id) + "</feldid>"
        xml += "</figur>"
        return xml
