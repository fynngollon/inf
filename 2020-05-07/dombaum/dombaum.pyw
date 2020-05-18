from xml.dom.minidom import *
from tkinter import *
import tkinter.filedialog

# Datenmodell

class DOMBaum(object):
    def __init__(self):
        self.aktuellerKnoten = None

baum = DOMBaum()

# GUI

# Ereignisverarbeitung

def knotenAnzeigen():
    labelWertNodeName.config(text=baum.aktuellerKnoten.nodeName)
    attributeString = ""
    attribute = baum.aktuellerKnoten.attributes
    if attribute != None:
        for i in range(attribute.length):
            attributeString = attributeString + attribute.item(i).nodeName + ': ' + attribute.item(i).nodeValue
            labelWertAttributes.config(text=attributeString)
    else:
        labelWertAttributes.config(text="")
    if baum.aktuellerKnoten.nodeValue != None:
        s=baum.aktuellerKnoten.nodeValue
    if baum.aktuellerKnoten.nodeName == '#text':
        s = s.replace(' ','\u23b5')
        s = s.replace('\n','\\n')
        s = s.replace('\t','\\t')
        labelWertNodeValue.config(text=s)
    else:
        labelWertNodeValue.config(text="")


def Button_parentNode_Click():
    if baum.aktuellerKnoten.parentNode != None:
        baum.aktuellerKnoten = baum.aktuellerKnoten.parentNode
    knotenAnzeigen()

def Button_previousSibling_Click():
    if baum.aktuellerKnoten.previousSibling != None:
        baum.aktuellerKnoten = baum.aktuellerKnoten.previousSibling
    knotenAnzeigen()

def Button_nextSibling_Click():
    if baum.aktuellerKnoten.nextSibling != None:
        baum.aktuellerKnoten = baum.aktuellerKnoten.nextSibling
    knotenAnzeigen()

def Button_firstChild_Click():
    if baum.aktuellerKnoten.firstChild != None:
        baum.aktuellerKnoten = baum.aktuellerKnoten.firstChild
    knotenAnzeigen()

def Button_lastChild_Click():
    if baum.aktuellerKnoten.lastChild != None:
        baum.aktuellerKnoten = baum.aktuellerKnoten.lastChild
    knotenAnzeigen()

def Button_quelltextLaden_Click():
    datei = tkinter.filedialog.askopenfile()
    textQuelltext.delete("1.0", END)
    if datei:
        textQuelltext.insert("1.0", datei.read())
        datei.close()

def Button_quelltextParsen_Click():
    xml_quelltext = textQuelltext.get("1.0", END)
    document = parseString(xml_quelltext)
    baum.aktuellerKnoten = document
    knotenAnzeigen()



# Erzeugung der Komponenten
# Fenster
tkFenster = Tk()
tkFenster.title("DOM-Baum")
tkFenster.geometry('415x500')

# Rahmen Quelltext
frameQuelltext = Frame(master=tkFenster, \
                  background="#BDE2F3")
frameQuelltext.place(x=10, y=10, width=395, height=235)

# Editor
scrollbar = Scrollbar(master=frameQuelltext)
scrollbar.place(x=375, y=10, width=10, height=185)
textQuelltext = Text(master=frameQuelltext, background="white", yscrollcommand=scrollbar.set)
textQuelltext.place(x=10, y=10, width=350, height=185)

# Button zum Laden und Parsen
buttonQuelltextLaden = Button(master=frameQuelltext, text="XML-Quelltext laden", command=Button_quelltextLaden_Click)
buttonQuelltextLaden.place(x=10, y=205, width=135, height=20)

buttonQuelltextParsen = Button(master=frameQuelltext, text="XML-Quelltext parsen", command=Button_quelltextParsen_Click)
buttonQuelltextParsen.place(x=250, y=205, width=135, height=20)

# Rahmen DOM-Baum
frameDOMBaum = Frame(master=tkFenster, \
                  background="gray")
frameDOMBaum.place(x=10, y=255, width=395, height=235)

# Button parentNode
buttonParentNode = Button(master=frameDOMBaum, \
                       text="parentNode", \
                       command=Button_parentNode_Click)
buttonParentNode.place(x=147, y=10, width=100, height=20)

# Button previousSibling
buttonPreviousSibling = Button(master=frameDOMBaum, \
                       text="previousSibling", \
                       command=Button_previousSibling_Click)
buttonPreviousSibling.place(x=10, y=45, width=100, height=20)

# Button nextSibling
buttonNextSibling = Button(master=frameDOMBaum, \
                       text="nextSibling", \
                       command=Button_nextSibling_Click)
buttonNextSibling.place(x=285, y=45, width=100, height=20)

# Button firstChild
buttonFirstChild = Button(master=frameDOMBaum, \
                       text="firstChild", \
                       command=Button_firstChild_Click)
buttonFirstChild.place(x=10, y=205, width=100, height=20)

# Button lastChild
buttonLastChild = Button(master=frameDOMBaum, \
                       text="lastChild", \
                       command=Button_lastChild_Click)
buttonLastChild.place(x=285, y=205, width=100, height=20)

# Rahmen aktueller Knoten
frameKnoten = Frame(master=frameDOMBaum, \
                  background="#D5E88F")
frameKnoten.place(x=120, y=40, width=155, height=155)
# Label mit Überschriften und Werten für den aktuellen Knoten
labelNodeName = Label(master=frameKnoten, \
                              text="nodeName", \
                              background="#D5E88F")
labelNodeName.place(x=5, y=5, width=145, height=20)

labelWertNodeName = Label(master=frameKnoten, \
                              text="", \
                              background="white")
labelWertNodeName.place(x=5, y=30, width=145, height=20)

labelAttributes = Label(master=frameKnoten, \
                              text="attributes", \
                              background="#D5E88F")
labelAttributes.place(x=5, y=55, width=145, height=20)

labelWertAttributes = Label(master=frameKnoten, \
                              text="", \
                              background="white")
labelWertAttributes.place(x=5, y=80, width=145, height=20)

labelNodeValue = Label(master=frameKnoten, \
                              text="nodeValue", \
                              background="#D5E88F")
labelNodeValue.place(x=5, y=105, width=145, height=20)

labelWertNodeValue = Label(master=frameKnoten, \
                              text="", \
                              background="white")
labelWertNodeValue.place(x=5, y=130, width=145, height=20)

# Aktivierung des Fensters
tkFenster.mainloop()
