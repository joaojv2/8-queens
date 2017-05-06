#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:28:13 2017

@author: joao
"""
from random import randint
from Mutacao import Mutacao
from Check import Check

class Reproducao(object):

	def __init__ (self , array1 , array2 , populacao , fitness ,  estadoInicial):
		self.array1 = array1
		self.array2 = array2
		self.populacao = populacao
		self.fitness = fitness
		self.estadoInicial = estadoInicial
		self.check = Check()

	def reproduzirFilho1(self):
		filho = self.array1[0:4]
		for i in self.array2:
			if i not in filho:
				filho.append(i)
		if randint(0 , 100) > 20:
			filho = Mutacao(filho).Mutacao()

		self.populacao.append(filho)
		self.fitness.append(self.check.fitness(filho , self.estadoInicial))

	def reproduzirFilho2(self):
		filho = self.array2[0:4]
		for i in self.array1:
			if i not in filho:
				filho.append(i)
		if randint(0 , 100) > 20:
			filho = Mutacao(filho).Mutacao()

		self.populacao.append(filho)
		self.fitness.append(self.check.fitness(filho , self.estadoInicial))