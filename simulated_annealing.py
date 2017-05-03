from random import random
from math import exp, expm1

def annealing ():
    
    s0 = 1000
    m = 1000 #numeros de intereçao
    p = 2 #numero maximo de perturbaçoes em cada iteraçao
    l = 1 #numero maximo de sucesso por iteraçoes
    alfa = 0.9 #fator de reducao de temperatura
    s = s0
    temp_start = 10000000
    t0 = temp_start
    t = t0
    j = 1

    while True:
        i = 1
        nSucess = 0
        while True:
            si = disturb(s)
            fi = si - s
            if fi <= 0 or exp(-fi / t) > randomizer():
                s = si
                nSucess = nSucess + 1
            i = i + 1 
            print(s)
            if nSucess >= l or i > p:
                break

        t = alfa * t
        j = j + 1

        if nSucess == 0 or j > m:
            break

    print(s)

def randomizer ():
    random_number = random()
    return random_number

def disturb(s):
    return s * 1.2

start_state = [0, 1 , 2 , 3 , 4 , 5 , 6 , 7]
annealing()