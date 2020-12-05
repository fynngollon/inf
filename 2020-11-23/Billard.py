from tkinter import *

def calc():
    allDifficulties = []
    # GesamtWinkel
    if int(entryGesamtWinkel.get()) > 1 and int(entryGesamtWinkel.get()) < 180:
        difficulty = 0
        for winkel in (171, 162, 153, 144, 135, 126, 117, 108, 99, 90):
            difficulty += 1
            if int(entryGesamtWinkel.get()) > winkel:
                lblGesamtWinkelS.config(text="Schwierigkeitsgrad: " + str(difficulty))
                allDifficulties += [difficulty]
                break;

    # Winkel 1
    if int(entryWinkel1.get()) > 0 and int(entryWinkel1.get()) < 180:
        difficulty = 0
        for winkel in (121.5, 108, 94.5, 81, 67.5, 54, 40.5, 27, 13.5, 1):
            difficulty += 1
            if int(entryWinkel1.get()) > winkel:
                lblWinkel1S.config(text="Schwierigkeitsgrad: " + str(difficulty))
                allDifficulties += [difficulty]
                break;


    # Abstand 1
    if int(entryAbstand1.get()) > 1 and int(entryAbstand1.get()) < 1000:
        difficulty = 0
        for abstand in (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10000):
            difficulty += 1
            if int(entryAbstand1.get()) < abstand:
                lblAbstand1S.config(text="Schwierigkeitsgrad: " + str(difficulty))
                allDifficulties += [difficulty]
                break;

    # Abstand 2
    if int(entryAbstand2.get()) > 1 and int(entryAbstand2.get()) < 1000:
        difficulty = 0
        for abstand in (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10000):
            difficulty += 1
            if int(entryAbstand2.get()) < abstand:
                lblAbstand2S.config(text="Schwierigkeitsgrad: " + str(difficulty))
                allDifficulties += [difficulty]
                break;
            

    # Konstellation
    if int(entryKonstellation.get()) >= 0 and int(entryKonstellation.get()) < 3:
        difficulty = 0
        for hindernisse in (0, 1, 2):
            difficulty += 1
            if int(entryKonstellation.get()) == hindernisse:
                lblKonstellationS.config(text="Schwierigkeitsgrad: " + str(difficulty))
                allDifficulties += [difficulty]
                break;

    # Verdeckt
    if int(entryVerdeckt.get()) >= 0 and int(entryVerdeckt.get()) < 100:
        difficulty = 0
        for prozent in (10, 20, 30, 40, 50, 60, 70, 80, 90, 100):
            difficulty += 1
            if int(entryVerdeckt.get()) < prozent:
                lblVerdecktS.config(text="Schwierigkeitsgrad: " + str(difficulty))
                allDifficulties += [difficulty]
                break;


    insgesamt = (allDifficulties[0]*3 + allDifficulties[1]*1 + allDifficulties[2]*1 + allDifficulties[3]*1 + allDifficulties[4]*2 + allDifficulties[5]*2) / 10
    lblErgebnis.config(text="Insgesamt: " + str(insgesamt))

# Variable:
widthLbl = 310
heightLbl = 20
widthEntry = 125
heightEntry = 20

xLbl = 5
xEntry = 320

root = Tk()
root.title("Billard-Schwierigkeitsgrad-Rechner")
root.geometry("610x270")

container = Frame(root,background="#555555").place(x=0, y=0, width=610, height=270)

frameInput = Frame(container).place(x=5, y=5, width=450, height=260)

frameOutput = Frame(container).place(x=460, y=5, width=145, height=260)

lblGesamtWinkel = Label(frameInput, text="Gesamtwinkel:").place(x=xLbl, y=15, width=widthLbl, height=heightLbl)
entryGesamtWinkel = Entry(frameInput)
entryGesamtWinkel.place(x=xEntry, y=15, width=widthEntry, height=heightEntry)

lblWinkel1 = Label(frameInput, text="Winkel 1: Angestoßene Kugel zu Loch:").place(x=xLbl, y=50, width=widthLbl, height=heightLbl)
entryWinkel1 = Entry(frameInput)
entryWinkel1.place(x=xEntry, y=50, width=widthEntry, height=heightEntry)

lblAbstand1 = Label(frameInput, text="Abstand Weiße Kugel zu angestoßene Kugel:").place(x=xLbl, y=85, width=widthLbl, height=heightLbl)
entryAbstand1 = Entry(frameInput)
entryAbstand1.place(x=xEntry, y=85, width=widthEntry, height=heightEntry)

lblAbstand2 = Label(frameInput, text="Abstand angestoßene Kugel zu Loch:").place(x=xLbl, y=120, width=widthLbl, height=heightLbl)
entryAbstand2 = Entry(frameInput)
entryAbstand2.place(x=xEntry, y=120, width=widthEntry, height=heightEntry)

lblKonstellation = Label(frameInput, text="Anzahl der Hinternisse:").place(x=xLbl, y=155, width=widthLbl, height=heightLbl)
entryKonstellation = Entry(frameInput)
entryKonstellation.place(x=xEntry, y=155, width=widthEntry, height=heightEntry)

lblVerdeckt = Label(frameInput, text="Prozentuale Verdeckung von Winkel 2 durch Hindernisse:").place(x=xLbl, y=190, width=widthLbl, height=heightLbl)
entryVerdeckt = Entry(frameInput)
entryVerdeckt.place(x=xEntry, y=190, width=widthEntry, height=heightEntry)

btnBerechnen = Button(frameInput, text="Schwierigkeitsgrad berechnen", background="#A9D0F5", command=calc).place(x=270, y=225, width=175, height=30)


# Ausgabe

lblGesamtWinkelS = Label(frameOutput, text="Schwierigkeitsgrad:")
lblGesamtWinkelS.place(x=465, y=15, width=135, height=heightLbl)

lblWinkel1S = Label(frameOutput, text="Schwierigsgkeitrad:")
lblWinkel1S.place(x=465, y=50, width=135, height=heightLbl)

lblAbstand1S = Label(frameOutput, text="Schwierigskeitgrad:")
lblAbstand1S.place(x=465, y=85, width=135, height=heightLbl)

lblAbstand2S = Label(frameOutput, text="Schwierigkeitsgrad:")
lblAbstand2S.place(x=465, y=120, width=135, height=heightLbl)

lblKonstellationS = Label(frameOutput, text="Schwierigskeitgrad:")
lblKonstellationS.place(x=465, y=155, width=135, height=heightLbl)

lblVerdecktS = Label(frameOutput, text="Schwierigskeitgrad:")
lblVerdecktS.place(x=465, y=190, width=135, height=heightLbl)

lblErgebnis = Label(frameOutput, text="")
lblErgebnis.place(x=465, y=225, width=135, height=20)

root.mainloop()
