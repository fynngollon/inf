from Kasse import *


class Spieler(object):
    """
    Die Spielfigur von chuck-a-luck.
    """
    def __init__(self, wliste, sf):
        """
        Erstellt einen Spieler mit eigener Kasse und übergibt ihm eine Liste von Würfeln sowie das Spielfeld.
        """
        self.kasse = Kasse()
        self.wuerfel = wliste
        self.spielfeld = sf
        self.name = ""

    def werfen(self):
        """
        Wirft alle dem Spieler bekannten Würfel.
        """
        for wuerfel in self.wuerfel:
            wuerfel.werfen()

    def auszahlen(self, betrag):
        """
        Zahlt einen Betrag aus der eigenen Kasse aus.
        Liefert True bei erfolgreicher Auszahlung zurück und False falls der Kontostand der Kasse nicht ausreicht.
        """
        return self.kasse.auszahlen(betrag)

    def einzahlen(self, gewinn):
        """
        Zahlt einen Gewinn in die eigene Kasse ein.
        """
        self.kasse.einzahlen(gewinn)
