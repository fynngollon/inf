from xml.dom.minidom import *

class Simulator(object):
    def __init__(self, jff, eingabe):
        f_xml = open(jff, "r")
        self.quelltext = f_xml.read()
        self.dombaum = parseString(self.quelltext)
        self.wurzel = self.dombaum.documentElement
        self.zustand = None

        self.currentPos = self.anfangszustand()
        #for line in eingabe:

    def anfangszustand(self):
        k_initial_liste = self.wurzel.getElementsByTagName("initial")
        if k_initial_liste != []:
            k_state = k_initial_liste[0].parentNode
            self.zustand = k_state.getAttribute("name")

    def naechsterzustand(self, eingabe):
            fromliste = baum.getElementsByTagName("from")
            for i in fromliste:
                if zustand == int(i.firstChild.nodeValue):
                    readliste = i.parentNode.getElementsByTagName("read")
                    for z in readliste:
                        if eingabe == z.firstChild.nodeValue:
                            transitionliste = i.parentNode.getElementsByTagName("to")
                            return int(transitionliste[0].firstChild.nodeValue)
            return False

    def endzustand(self):
            k_state_liste = baum.getElementsByTagName("state")
            for i in k_state_liste:
                if zustand == int(i.getAttribute("id")):
                    final = i.getElementsByTagName("final")
                    if final != []:
                        return True
                    else:
                        return False
            return False

    def getZustand(self):
        return self.zustand
