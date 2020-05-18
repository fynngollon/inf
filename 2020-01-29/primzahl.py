def primzahl(n):
    if n == 1:
        prim = False
    else:
        prim = True
        i = 2
        while i < n:
            if n % i == 0:
                prim = False
            i += 1
            
    return prim
