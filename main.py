#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hillClimbing as climb

def main():

    #Pega a matriz do arquivo
    matriz = climb.getMatrizArquivo('matriz.txt')
    #Cria o objeto
    hc = climb.HillClimbing()
    #Init da matriz no objeto
    hc.setMatriz(matriz)
    print "\nMatriz inicial\n"
    #Imprime a matriz Inicial
    climb.imprimeMatriz(matriz)
    print "Quantidade de ataques entre pares de rainhas:" + str(climb.getTotalAtackTabuleiro(matriz))
    print "---------------------------------------"
    #imprime a matriz com o resultado
    climb.imprimeMatriz(hc.hill(20))
main()
