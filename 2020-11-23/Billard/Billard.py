from tkinter import *



# Variable:
widthLbl = 230
heightLbl = 20
widthEntry = 105
heightEntry = 20

xLbl = 5
xEntry = 270




root = Tk()
root.title("Billard-Schwierigkeitsgrad-Rechner")
root.geometry("775x300")

container = Frame(root, background="#555555").place(x=0, y=0, width=720, height=300)

frameInput = Frame(container).place(x=5, y=5, width=380, height=290)

frameOutput = Frame(container).place(x=390, y=5, width=380, height=290)


lblGesamtWinkel = Label(frameInput, text="Gesamtwinkel:").place(x=xLbl, y=15, width=widthLbl, height=heightLbl)
entryGesamtWinkel = Entry(frameInput).place(x=xEntry, y=15, width=widthEntry, height=heightEntry)

lblWinkel2 = Label(frameInput, text="Winkel 2: Kugel 2 zu Loch:").place(x=xLbl, y=85, width=widthLbl, height=heightLbl)
entryWinkel2 = Entry(frameInput).place(x=xEntry, y=85, width=widthEntry, height=heightEntry)

lblAbstand1 = Label(frameInput, text="Abstand Weiße Kugel zu angestoßene Kugel:").place(x=xLbl, y=120, width=widthLbl, height=heightLbl)
entryAbstand1 = Entry(frameInput).place(x=xEntry, y=120, width=widthEntry, height=heightEntry)

lblAbstand2 = Label(frameInput, text="Abstand angestoßene Kugel zu Loch:").place(x=xLbl, y=155, width=widthLbl, height=heightLbl)
entryAbstand2 = Entry(frameInput).place(x=xEntry, y=155, width=widthEntry, height=heightEntry)

lblKonstellation = Label(frameInput, text="Anzahl der Hinternisse:").place(x=xLbl, y=190, width=widthLbl, height=heightLbl)
entryKonstellation = Entry(frameInput).place(x=xEntry, y=190, width=widthEntry, height=heightEntry)

lblVerdeckt = Label(frameInput, text="Prozentuale Verdeckung von Winkel 2 durch Hindernisse:").place(x=xLbl, y=225, width=widthLbl, height=heightLbl)
entryVerdeckt = Entry(frameInput).place(x=xEntry, y=225, width=widthEntry, height=heightEntry)

btnBerechnen = Button(frameInput, text="Schwierigkeitsgrad berechnen").place(x=200, y=260, width=175, height=30)


# Ausgabe

##lblGesamtWinkelS = Label(frameOutput, text="GesamtwinkelS:").place(x=5, y=15, width=widthLbl, height=heightLbl)
##entryGesamtWinkelS = Entry(frameOutput).place(x=210, y=15, width=widthEntry, height=heightEntry)
##
##lblWinkel1S = Label(frameOutput, text="Winkel 1: Weiße Kugel zu Kugel 2:").place(x=5, y=50, width=widthLbl, height=heightLbl)
##entryWinkel1S = Entry(frameOutput).place(x=210, y=50, width=widthEntry, height=heightEntry)
##
##lblWinkel2S = Label(frameOutput, text="Winkel 2: Kugel 2 zu Loch:").place(x=5, y=85, width=widthLbl, height=heightLbl)
##entryWinkel2S = Entry(frameOutput).place(x=210, y=85, width=widthEntry, height=heightEntry)
##
##lblAbstand1S = Label(frameOutput, text="Abstand Weiße Kugel zu Kugel 2:").place(x=5, y=120, width=widthLbl, height=heightLbl)
##entryAbstand1S = Entry(frameOutput).place(x=210, y=120, width=widthEntry, height=heightEntry)
##
##lblAbstand2S = Label(frameOutput, text="Abstand Kugel 2 zu Loch:").place(x=5, y=155, width=widthLbl, height=heightLbl)
##entryAbstand2S = Entry(frameOutput).place(x=210, y=155, width=widthEntry, height=heightEntry)
##
##lblKonstellationS = Label(frameOutput, text="Kontellation").place(x=5, y=190, width=widthLbl, height=heightLbl)
##entryKonstellationS = Entry(frameInput).place(x=210, y=190, width=widthEntry, height=heightEntry)
##
##lblVerdecktS = Label(frameOutput, text="Winkel 2 durch Konstellation verdeckt:").place(x=5, y=225, width=widthLbl, height=heightLbl)
##entryVerdecktS = Entry(frameOutput).place(x=210, y=225, width=widthEntry, height=heightEntry)
##
##lblErgebnis = Label(frameOutput, text="").place(x=5, y=260, width=200, height=20)


root.mainloop()
