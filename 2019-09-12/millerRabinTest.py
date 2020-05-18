from random import randint

def millerRabinTest(n):
    aList = []

    # 1. Berechne s
    s = 0
    n_temp = n-1
    while (n_temp) % 2 == 0:
        n_temp /= 2
        s += 1

    # 2. Berechne d
    d = (n-1)//2**s

    while len(aList) + 3 < n and len(aList) < 10:
    
        # 3. Waehle a
        a = randint(3, n-1)
        while a in aList:
            a = randint(3, n-1)

        aList.append(a)

        # 4. Theorem
        if a**d % n == 1:
            continue

        r = -1
        for counter in range(0, s):
            if a**(2**counter*d) % n == n-1:
                r = counter
                break

        if r >= 0:
            continue
        
        return False

    return True


