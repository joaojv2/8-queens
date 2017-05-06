#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import hillClimbing as climb
from AlgoritmoGenetico import AlgoritmoGenetico
from SimulatedAnnealing import SimulatedAnnealing
import hillClimbing as climb
def main():
	tipo = "algoritmo genetico"

	if tipo == "hill climb":
		#Pega a matriz do arquivo
	    matriz = climb.getMatrizArquivo('matriz.txt')
	    #Cria o objeto
	    hc = climb.HillClimbing()
	    #Init da matriz no objeto
	    hc.setMatriz(matriz)
	    print ("\nMatriz inicial\n")
	    #Imprime a matriz Inicial
	    climb.imprimeMatriz(matriz)
	    print ("Quantidade de ataques entre pares de rainhas:" + str(climb.getTotalAtackTabuleiro(matriz)))
	    print ("---------------------------------------")
	    #imprime a matriz com o resultado
	    climb.imprimeMatriz(hc.hill(20))

	elif tipo == "simulated annealing":
		simulatedannealing = SimulatedAnnealing()

	elif tipo == "algoritmo genetico":
		algoritmogenetico = AlgoritmoGenetico()
main()
