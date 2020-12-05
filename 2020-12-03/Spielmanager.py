from Spielfeld import *
from Spieler import *
from Wuerfel import *


class Spielmanager(object):
    """
    Controller für chuck-a-luck
    """
    def __init__(self):
        """
        Initialisierung des Spielmanagers.
        Erstellt drei Würfel, das Spielfeld und den Spieler.
        """
        self.w1 = Wuerfel()
        self.w2 = Wuerfel()
        self.w3 = Wuerfel()
        self.spielfeld = Spielfeld()
        self.spieler = Spieler([self.w1, self.w2, self.w3], self.spielfeld)

    def spielen(self, gesetzteZahl, betrag):
        """
        Führt eine Runde chuck-a-luck durch.
        """
        if self.spieler.kasse.auszahlen(betrag):
            self.spielfeld.setzen(gesetzteZahl)
            self.spieler.werfen()
            if (auswertung := self.auswerten()) > 0:
                self.gewinnAuszahlen(betrag * auswertung + betrag)
                print("Du hast " + str(auswertung) + " Übereinstimmungen und damit " +
                      str(betrag * auswertung) + " Gewinn gemacht!\nNeuer Kontostand: " +
                      str(self.spieler.kasse.getKontostand()))
            else:
                print("Es gab keine Übereinstimmungen.\nNeuer Kontostand: " +
                      str(self.spieler.kasse.getKontostand()))
        else:
            print("Du hast wohl den Überblick über dein Geld verloren!\nDu kannst maximal " +
                  str(self.spieler.kasse.getKontostand()) + " einsetzen.")

    def gewinnAuszahlen(self, betrag):
        """
        Zahlt dem Spieler den Gewinn aus.
        """
        self.spieler.einzahlen(betrag)

    def auswerten(self):
        """
        Gibt die Übereinstimmung von gesetzter Zahl und Würfelaugen aus.
        """
        uebereinstimmung = 0
        for augen in self.getAugen():
            if augen == self.spielfeld.getGesetzteZahl():
                uebereinstimmung += 1
        return uebereinstimmung

    def getAugen(self):
        """
        Gibt die Augenzahlen der Würfel in einer Liste aus.
        """
        return [self.w1.getAugen(), self.w2.getAugen(), self.w3.getAugen()]

