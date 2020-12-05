class Spielfeld(object):
    """
    Spielfeld von chuck-a-luck (mit 6 Feldern).
    """
    def __init__(self):
        """
        Erstellt ein Spielfeld mit dem Attribut gesetzteZahl, um zu speichern auf welchen Feld der Spiel setzen will.
        """
        self.gesetzteZahl = 1

    def setzen(self, zahl):
        """
        Setzt den Einsatz auf die übergebene Zahl, falls diese zwischen einschließlich 1 und 6 liegt.
        """
        if 0 < zahl < 7:
            self.gesetzteZahl = zahl

    def getGesetzteZahl(self):
        """
        Gibt die Zahl zurück, auf die gesetzt wurde.
        """
        return self.gesetzteZahl
