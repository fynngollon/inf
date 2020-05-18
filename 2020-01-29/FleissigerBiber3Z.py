for counter in range (0, 16**6):
    # Konvertiere Zahl in binär
    binaer = bin(counter)[2:].zfill(24)
    print("\nTuringmaschine '" + str(binaer) + "' (" + str(int(binaer, 2)+1) + " von " + str(16**6) + "):")

    # Binärzahl verarbeiten
    for indices in ([0,4],[4,8],[8,12],[12,16],[16,20],[20,24]):
        # Binärzahl in Viererblock aufteilen
        sub_binaer = binaer[indices[0]:indices[1]]
        # Bsp.: '        0 00 0'
        #       'q0 0 -> 0 q0 L' (weitere Infos s.u.)
        print("q" + str(indices[0]//8), ("0" if indices[0]%8==0 else "1"), "->", sub_binaer[0], "q" + str(int(sub_binaer[1:3], 2)), ("L" if sub_binaer[3]=="0" else "R"))



        # Zustand 1:    jede zweite Liste erhöht Wert um 1 ->   'q0, q0, q1, q1, q2, q2'
        # Bandsymbol 1: wechselt zwischen 0 und 1 ->            ' 0,  1,  0,  1,  0,  1'
        # Bandsymbol 2: 1. Binärzahl vom Substring
        # Zustand 2:    2. & 3. Binärzahl vom Substring in Dezimalzahl umgeformt
        # Richtung:     4. Binärzahl vom Substring == 0 -> Links; == 1 -> Rechts
