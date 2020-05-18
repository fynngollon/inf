def codierungZeichen(zeichen, abc):

    """ 
    >>> codierungZeichen('A', ' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    1
    """

    return abc.index(zeichen)

def decodierungZahl(zahl, abc):

    """ 
    >>> decodierungZahl(1, ' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    'A'
    """
    
    return abc[zahl]


def zerlegung(wort, blocklaenge):

    """ 
    >>> zerlegung('TEST', 2)
    ['TE', 'ST']

    >>> zerlegung('HALLO', 3)
    ['HAL', 'LO ']

    >>> zerlegung('HALLO', 2)
    ['HA', 'LL', 'O ']

    >>> zerlegung('', 4)
    []
    """
    
    liste = []
    block = ''
    for c in wort:
        if len(block) == blocklaenge:
            liste = liste + [block]
            block = ''
        block = block + c
    if block != '':
        fehlend = blocklaenge - len(block)
        block = block + fehlend * ' '
        liste = liste + [block]
    return liste

def codierungBlock(wort, abc):

    """ 
    >>> codierungBlock('BAD', ' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    20104
   
    >>> codierungBlock('O ', ' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    1500
    """
    
    hilfszahl = 0
    for c in wort:
        hilfszahl = hilfszahl*100 + codierungZeichen(c, abc)
    return hilfszahl

    
def codierungBlockListe(blockListe, abc):

    """ 
    >>> codierungBlockListe(['HA', 'LL', 'O '], ' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    [801, 1212, 1500]
    """
    
    liste = []
    for block in blockListe:
        liste = liste + [codierungBlock(block, abc)]
    return liste

def codierung(wort, blocklaenge, abc):

    """ 
    >>> codierung('HALLO', 2, ' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    [801, 1212, 1500]
    """
    
    return codierungBlockListe(zerlegung(wort, blocklaenge), abc)

def decodierungBlockcodierung(zahl, blocklaenge, abc):

    """ 
    >>> decodierungBlockcodierung(10203, 3, ' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    'ABC'
    """
    
    wort = ''
    while blocklaenge > 0:
        rest = zahl % (10**2)
        wort = decodierungZahl(rest, abc) + wort
        zahl = zahl // (10**2)
        blocklaenge = blocklaenge - 1
    return wort
    
def decodierungListeBlockcodierung(zahlenListe, blocklaenge, abc):

    """ 
    >>> decodierungListeBlockcodierung([801, 1212, 1500], 2, ' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ['HA', 'LL', 'O ']
    """
    
    liste = []
    for zahl in zahlenListe:
        liste = liste + [decodierungBlockcodierung(zahl, blocklaenge, abc)]
    return liste

def zusammenfuegung(liste):

    """ 
    >>> zusammenfuegung(['HA', 'LL', 'O '])
    'HALLO'
    """
    
    ergebnis = ''
    listeOhneLetztesWort = liste[:len(liste)-1]
    letztesWort = liste[len(liste)-1]
    for wort in listeOhneLetztesWort:
        ergebnis = ergebnis + wort
    # Leerzeichen am Ende entfernen
    m = len(letztesWort)-1
    gefunden = False
    while m >= 0 and not gefunden:
        c = letztesWort[m]
        if c != ' ':
            gefunden = True
        else:
            m = m-1
    letztesWort = letztesWort[0:m+1]
    ergebnis = ergebnis + letztesWort
    return ergebnis

def decodierung(zahlenListe, blocklaenge, abc):

    """ 
    >>> decodierung([801, 1212, 1500], 2, ' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    'HALLO'
    """
    
    return zusammenfuegung(decodierungListeBlockcodierung(zahlenListe, blocklaenge, abc))

def modpot(x, y, m):
    
    """
    >>> modpot(52, 37, 77)
    24
    """
    pot = 1
    while y > 0:
        if y % 2 == 1:
            pot = (pot * x) % m
            y = y - 1
        else:
            x = (x * x) % m
            y = y // 2
    return pot

def verschluesselteZahl(zahl, schluessel):

    """
    >>> verschluesselteZahl(19, (13, 77))
    61
    """
    
    return modpot(zahl, schluessel[0], schluessel[1])

def verschluesselung(zahlenListe, schluessel):

    """ 
    >>> verschluesselung([1, 19, 20, 5, 18, 9, 24], (13, 77))
    [1, 61, 69, 26, 46, 58, 52]
    >>> verschluesselung([1, 61, 69, 26, 46, 58, 52], (37, 77))
    [1, 19, 20, 5, 18, 9, 24]
    """

    liste = []
    for zahl in zahlenListe:
        liste = liste + [verschluesselteZahl(zahl, schluessel)]
    return liste

# Test

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=False)
