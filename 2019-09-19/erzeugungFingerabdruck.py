def zahl(c):
    
    """
    >>> zahl('A')
    1
    """
    
    if c == ' ':
        return 0
    else:
        return ord(c)-65+1

def fingerabdruck(text):
    
    """
    >>> fingerabdruck('HALLO')
    21
    """

    summe = 0
    for zeichen in text:
        summe = summe + zahl(zeichen)
    return summe % 27

