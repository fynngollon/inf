from random import randint


class Wuerfel(object):
    """
    Würfel, um eine Zufällszahl zwischen 1 und 6 zu erhalten.
    """
    def __init__(self):
        """
        Erstellt einen Würfel mit dem Attribut augen
        """
        self.augen = 1

    def werfen(self):
        """
        Setzt das die Augenzahl des Würfels auf einen zufälligen Wert zwischen 1 und 6.
        """
        self.augen = randint(1, 6)

    def getAugen(self):
        """
        Gibt die Augenzahl des Würfels zurück.
        """
        return self.augen
