for c in range (0, 16**6):
    for i in ([0,4],[4,8],[8,12],[12,16],[16,20],[20,24]):
        print("q" + str(i[0]//8), "0" if i[0]%8==0 else "1", "->", bin(c)[2:].zfill(24)[i[0]:i[1]][0], "q" + str(int(bin(c)[2:].zfill(24)[i[0]:i[1]][1:3], 2)), "L" if bin(c)[2:].zfill(24)[i[0]:i[1]][3]=="0" else "R", "\n" if i[1]==24 else "")