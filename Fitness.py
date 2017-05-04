#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:28:13 2017

@author: joao
"""
from VerificarTabuleiro import VerificarTabuleiro

class Fitness(object):
    def __init__(self , tabuleiro):
        self.tabuleiro = tabuleiro
        self.fitness = 0
        self.setFitness()
    
    def getFitness(self):
        return self.fitness
    
    def setFitness(self):
        self.fitness = VerificarTabuleiro(self.tabuleiro , self.fitness).verificarTabuleiro()