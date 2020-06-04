from xml.dom.minidom import *

class Automat(object):
    def __init__(self, quelltext):
        self.quelltext = quelltext
        self.dombaum = parseString(self.quelltext)
        self.wurzel = self.dombaum.documentElement
        self.zustand = None

    def anfangszustand(self):
        k_initial_liste = self.wurzel.getElementsByTagName("initial")
        if k_initial_liste != []:
            k_state = k_initial_liste[0].parentNode
            self.zustand = int(k_state.getAttribute("id"))

    def naechsterzustand(self, eingabe):
        fromliste = self.wurzel.getElementsByTagName("from")
        for i in fromliste:
            if self.zustand == int(i.firstChild.nodeValue):
                readliste = i.parentNode.getElementsByTagName("read")
                for z in readliste:
                    if eingabe == z.firstChild.nodeValue:
                        transitionliste = i.parentNode.getElementsByTagName("to")
                        self.zustand = int(transitionliste[0].firstChild.nodeValue)
                        return int(transitionliste[0].firstChild.nodeValue)
        return None

    def endzustand(self):
        k_state_liste = self.wurzel.getElementsByTagName("state")
        for i in k_state_liste:
            if self.zustand == int(i.getAttribute("id")):
                final = i.getElementsByTagName("final")
                if final != []:
                    return True
                else:
                    return False
        return False

    def getZustand(self):
        return self.zustand

# Test
f_xml = open("email.jff", "r")
xml_quelltext = f_xml.read()

automat = Automat(xml_quelltext)

automat.anfangszustand()
print(automat.getZustand())
automat.naechsterzustand("b")
