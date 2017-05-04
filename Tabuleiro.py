#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:28:13 2017

@author: joao
"""
import random 

class Tabuleiro(object):
    def __init__(self):
        self.linha = []
        self.coluna = []
        self.GerarTabuleiro()
        
    def GerarTabuleiro(self):
        for i in range(8):
            valor = random.randrange(0,8)
            for j in range(8):
                if j == valor:
                    self.coluna.append(1)
                else:
                    self.coluna.append(0)
            self.linha.append(self.coluna)
            self.coluna = []
    
    def imprimirTabuleiro(self):
        for i in range(8):
            print(self.linha[i])