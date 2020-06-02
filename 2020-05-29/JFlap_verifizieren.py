from xml.dom.minidom import *

# Anfangszustand
def anfangszustand(baum):
    z = None
    k_initial_liste = baum.getElementsByTagName("initial")
    if k_initial_liste != []:
        k_state = k_initial_liste[0].parentNode
        z = int(k_state.getAttribute("id"))
    return z

# nächster Zustand
def naechsterzustand(baum, zustand, eingabe):
    fromliste = baum.getElementsByTagName("from")
    for i in fromliste:
        if zustand == int(i.firstChild.nodeValue):
            readliste = i.parentNode.getElementsByTagName("read")
            for z in readliste:
                if eingabe == z.firstChild.nodeValue:
                    transitionliste = i.parentNode.getElementsByTagName("to")
                    return int(transitionliste[0].firstChild.nodeValue)
    return False


# Endzustand
def endzustand(baum, zustand):
    k_state_liste = baum.getElementsByTagName("state")
    for i in k_state_liste:
        if zustand == int(i.getAttribute("id")):
            final = i.getElementsByTagName("final")
            if final != []:
                return True
            else:
                return False
    return False

# Einlesen des XML-Quelltextes
f_xml = open("email.jff", "r")
xml_quelltext = f_xml.read()

# Initialisierung des DOM-Baums
dombaum = parseString(xml_quelltext)
wurzel = dombaum.documentElement

# Test
z = anfangszustand(wurzel)
print(z)
wort = "bbb@b.bb"
for w in wort:
    z = naechsterzustand(wurzel, z, w)
    print(z)
if endzustand(wurzel, z):
    print("akzeptiert")
else:
    print("nicht akzeptiert")
