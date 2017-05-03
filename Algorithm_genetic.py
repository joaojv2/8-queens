# -*- coding: utf-8 -*-
"""
Created on Tue May  2 13:24:12 2017

@author: João Victor
"""

from random import randint

board=[1,2,3,4,5,6,7,8]

# Função para vereficar quantidade de colisões
def check(array):
 
    collisions = 0
    for i in range(1,9):
        if i not in array:
            print ("ERROR")
            return 0

    for i in range(0, 8):
        col = 0
        for j in range(0, 8):
            if i != j:
                if abs(board[i]-board[j]) == abs(array[j]-array[i]):
                    col = 1
        if col == 1:
            collisions += 1
    return 8-collisions

def reproduce(array1, array2):
 
    baby = array1[0:4]
    for i in array2:
        if i not in baby:
            baby.append(i)
    if randint(0,100) > 20:
        baby = mutate(baby)
    population.append(baby)
    fitness.append(check(baby))
 
    baby = array2[0:4]
    for i in array1:
        if i not in baby:
            baby.append(i)

    if randint(0,100)  > 20:
        baby = mutate(baby)

    population.append(baby)
    fitness.append(check(baby)) 
 
def mutate(array1):
    a = randint(0,7)
    b = randint(0,7)
    c = array1[a]
    array1[a]= array1[b]
    array1[b]=c
    return array1

def printpop():
    for i in range(0, len(population)):
        print (population[i],fitness[i])

popsize = 40
variation = [4,14]  
die = 0.40 
kill_limit = die * popsize

population=[]
fitness=[]
best_result = False

for i in range(0,popsize):
    population.append([1,2,3,4,5,6,7,8])

    a = 0

    while a < randint(variation[0],variation[1]):
        a += 1
        population[i]=mutate(population[i])
    fitness.append(check(population[i]))


maxi = 0
generations = 1

while maxi != 8:
 
    killed = 0
    x = 0
    while killed < kill_limit:
        for i in range(0,popsize):
            try:
                if fitness[i] == x:
                    population.pop(i)
                    fitness.pop(i)
                    killed += 1

                if killed==kill_limit:
                    break
            except:
                break
        x += 1
 
        babies = 0 
        cpop = len(population)-1 

        while babies < killed:
            reproduce(population[randint(0,cpop)],population[randint(0,cpop)])
            babies+=2 

        generations += 1

        maxi = 0
        for i in range(0,popsize):
            if fitness[i] > maxi:
                maxi = fitness[i]
                if maxi == 8:
                    print ("best solution :" , population[i])
                    best_result = True
                    break
        if best_result == True:
            break