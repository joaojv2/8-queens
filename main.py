#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from AlgoritmoGenetico import AlgoritmoGenetico
from SimulatedAnnealing import SimulatedAnnealing
import hillClimbing as climb

def main():
	print("Digite o tipo de resolução desejada:")
	print("1-Simulated Annealing 2-Algoritmo Genetico 3-Hill Climbing")
	tipo = input()

	inicio = time.time()
	corrente = time.time() - inicio
	if tipo == '3':
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
	elif tipo == '1':
		simulatedannealing = SimulatedAnnealing('matriz.txt')

	elif tipo == '2':
		algoritmogenetico = AlgoritmoGenetico('matriz.txt')
    
	else:
		print("Função não encontrada\n");
	
	decorrido = time.time() - inicio
	print("\nTempo de execução:",decorrido, "segundos" )
		
main()
