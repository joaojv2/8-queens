#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:28:13 2017

@author: joao
"""
from Reproducao import Reproducao
from Check import Check
from Arquivo import Arquivo
from Mutacao import Mutacao
from random import randint

class AlgoritmoGenetico(object):

	def __init__(self , path):
		self.estadoInicial = [1,2,3,4,5,6,7,8]
		self.tamanhoPopulacao = 40
		self.variacao = [4,14]  
		self.morte = 0.40 
		self.morteLimite = self.morte * self.tamanhoPopulacao
		self.path = path
		self.arquivo = Arquivo()

		self.populacao=[]
		self.fitness=[]
		self.melhorResultado = False
		self.check = Check()

		self.executavel()

	def imprimeMatriz(self , matriz):
		print("------Matriz inicial-------")
		for i in range(len(matriz)):
			linha = matriz[i]
			print(linha)

	def executavel(self):
		S0 = self.arquivo.getMatrizArquivo(self.path)
		self.imprimeMatriz(S0)
		for i in range(0 , self.tamanhoPopulacao):
			self.populacao.append([1,2,3,4,5,6,7,8])
			a = 0
			while a < randint(self.variacao[0] , self.variacao[1]):
				a += 1
				self.populacao[i] = Mutacao(self.populacao[i]).Mutacao()

			fitness_final = self.check.fitness(self.populacao[i] , self.estadoInicial)	
			self.fitness.append(fitness_final)
		maxi = 0
		geracao = 1

		while maxi != 8:
 
		    morto = 0
		    x = 0
		    while morto < self.morteLimite:
		        for i in range(0 , self.tamanhoPopulacao):
		            try:
		                if self.fitness[i] == x:
		                    self.populacao.pop(i)
		                    self.fitness.pop(i)
		                    morto += 1

		                if morto == self.morteLimite:
		                    break
		            except:
		                break
		        x += 1
		 
		        filhos = 0 
		        cpop = len(self.populacao)-1 

		        while filhos < morto:
		            reproducao = Reproducao(self.populacao[randint(0,cpop)],self.populacao[randint(0,cpop)] , self.populacao , self.fitness , self.estadoInicial)
		            reproducao.reproduzirFilho1()
		            reproducao.reproduzirFilho2()
		            filhos += 2 

		        geracao += 1

		        maxi = 0
		        for i in range(0 , self.tamanhoPopulacao):
		            if self.fitness[i] > maxi:
		                maxi = self.fitness[i]
		                if maxi == 8:
		                	print("Algoritmo Genetico")
		                	print(self.populacao[i])
		                	self.melhorResultado = True
		                	break
		        if self.melhorResultado == True:
		            break