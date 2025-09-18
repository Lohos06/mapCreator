import random

N = 0
Random = random.randint(1, 1000)

while N != Random :
    print("Choisissez un nombre")
    N = int(input())

    if N > Random :
        print("trop grand")
    elif N < Random :
        print("trop petit")
    else : 
        print ("bravo, c'etait", N)
        break