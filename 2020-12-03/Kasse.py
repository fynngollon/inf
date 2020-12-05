class Kasse(object):
    """
    Verwaltet das Geld des Spielers.
    """
    def __init__(self):
        """
        Erstellt eine Kasse mit 100 [Währung] als Anfangsguthaben.
        """
        self.kontostand = 100

    def einzahlen(self, gewinn):
        """
        Erhöht den Kontostand der Kasse um den übergebenen Wert.
        """
        if gewinn > 0:
            self.kontostand += gewinn

    def auszahlen(self, betrag):
        """
        Verringert den Kontostand der Kasse um den übergebenen Wert.
        """
        if betrag > 0:
            if self.kontostand - betrag >= 0:
                self.kontostand -= betrag
                return True
        return False

    def getKontostand(self):
        """
        Gibt den aktuellen Kontostand aus.
        """
        return self.kontostand
