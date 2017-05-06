#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:28:13 2017

@author: joao
"""
from Tabuleiro import Tabuleiro
from Fitness import Fitness
from Arquivo import Arquivo
import math
import random

class SimulatedAnnealing(object):

    def __init__ (self , path):
        self.path = path
        self.arquivo = Arquivo()
        self.main()

    def aceitacaoNovaSolucao(self ,temperatura , delta):
        if delta <= 0:
            return True
        numeroRandom = random.random()
        numero = math.exp(-delta / temperatura)
        if numero > numeroRandom:
            return True    
        return False

    def temperaturaInicial (self):
        return 1000

    def imprimirMatrizInicial(self , S0):
        print("------Matriz inicial-------")
        for i in range(len(S0)):
            linha = S0[i]
            print(linha)


    def main(self):
        alpha = 0.2
        S0 = self.arquivo.getMatrizArquivo(self.path)
        self.imprimirMatrizInicial(S0)
        S = 0
        T0 = self.temperaturaInicial()
        T = T0
        j = 1
        while True:
            i = 1
            while True:
                S0 = Tabuleiro()
                fitness = Fitness(S0)
                novaTemperatura = fitness.getFitness()
                delta = novaTemperatura - T
                if self.aceitacaoNovaSolucao(T , delta) == True:
                    S = S0
                    T = novaTemperatura
                i += 1
                if i == 10000 or T == 0:
                    break
            T = T * alpha
            j += 1
            if T <= 0:
                break
        
        print("Simulated Annealing Resultado:")
        S.imprimirTabuleiro()