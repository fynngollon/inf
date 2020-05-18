text = ""
file = open("text.txt", "r")
for line in file:
    text += line
file.close()

def haeufigkeitsanalyse(text):
    letterList = [0]*26
    
    for letter in range(0, len(text)):
        if ord(text[letter]) >= 65 and ord(text[letter]) <= 90:
            letterList[ord(text[letter])-65] += 1
        
    return letterList


print(haeufigkeitsanalyse(text))


def prozentualeAusgabe(letterList):
    char = 65
    anzahlChars = 0
    for anzahl in letterList:
        anzahlChars += anzahl
        
    for letter in letterList:
        print(chr(char), ":", ((letter * 100)/ anzahlChars), "%")
        char += 1
