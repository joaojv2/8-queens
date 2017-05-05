#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
from heapq import heappush, heappop

class HillClimbing(object):

    def __init__(self, matriz =[]):
        self.matriz = matriz

    def setMatriz(self, matriz):
        self.matriz = matriz

    def hill(self, iteracoes):
        count = 0
        listaPossivel = listaTabuleiroMovimentosPossiveis(self.matriz)
        totalAtackAtual = -1;

        while totalAtackAtual != 0 and count < iteracoes :
            #possivel proximo tabuleiro
            listaPossivel = []
            listaPossivel = listaTabuleiroMovimentosPossiveis(self.matriz)
            totalAtackAtual = getTotalAtackTabuleiro(self.matriz)
            #print totalAtackAtual
            possivelTabuleiro = listaPossivel[0][1]
            if  getTotalAtackTabuleiro(possivelTabuleiro) < totalAtackAtual:
                self.matriz = possivelTabuleiro
                heappop(listaPossivel)

            count += 1

        print "Quantidade de iteracoes: " + str(count)
        print "Quantidade de ataques entre pares de rainhas:" + str(totalAtackAtual)
        return self.matriz



def lerArquivo(path):
    conteudoArquivo = open(path, "r")
    return conteudoArquivo

#Pega matriz Arquivo
def getMatrizArquivo(pathArquivo):
    conteudoArquivo = lerArquivo(pathArquivo)
    matriz = []
    for linhaArquivo in conteudoArquivo:
        valores = linhaArquivo.replace("\n", "").split(' ')
        linha = []
        for valor in valores:
            linha.append(valor)
        matriz.append(linha)
    return matriz

def posicaoElementoColunaMatriz(matriz, elemento, coluna):
    for j in range(len(matriz)):
        if matriz[j][coluna] == elemento:
            return j

# Retorna a posicao das rainhas na matriz
def getPosicoesElentoMatriz(matriz, elemento):
    listaRainhas = []
    for i in range(len(matriz)):
        linha = matriz[i]
        for j in range(len(linha)):
            if matriz[i][j] == elemento:
                aux = str(i) + ' ' + str(j)
                listaRainhas.append(aux)
    return listaRainhas

#Função que percorre a diagonal secundaria superior em busca de algum conflito
def verificaDiagonalSecundariaSuperior(tabuleiro, posicaoI, posicaoJ):
    aux = 0
    for aux in range(len(tabuleiro)):
        posicaoI  = posicaoI - 1
        posicaoJ  = posicaoJ + 1
        if posicaoI >= 0 and posicaoJ < len(tabuleiro):
            if tabuleiro[posicaoI][posicaoJ] != '0':
                #print "Diagonal inferior"
                return 1
        else:
            return 0
#Função que percorre a diagonal inferior em busca de algum conflito
def verificaDiagonalSecundariaInferior(tabuleiro, posicaoI, posicaoJ):
    aux = 0
    for aux in range(len(tabuleiro)):
        posicaoI  = posicaoI + 1
        posicaoJ  = posicaoJ - 1
        if posicaoI < len(tabuleiro) and posicaoJ >= 0:
            if tabuleiro[posicaoI][posicaoJ] != '0':
                #print "Diagonal inferior"
                return 1
        else:
            return 0

#Função que percorre a diagonal inferior em busca de algum conflito
def verificaDiagonalPrincipalInferior(tabuleiro, posicaoI, posicaoJ):
    aux = 0
    for aux in range(len(tabuleiro)):
        posicaoI  = posicaoI + 1
        posicaoJ  = posicaoJ + 1
        if posicaoI < len(tabuleiro) and posicaoJ < len(tabuleiro):
            if tabuleiro[posicaoI][posicaoJ] != '0':
                #print "Diagonal inferior"
                return 1
        else:
            return 0

#Função que percorre a diagonal superior em busca de algum conflito
def verificaDiagonalPrincipalSuperior(tabuleiro, posicaoI, posicaoJ):
    aux = 0
    for aux in range(len(tabuleiro)):
        posicaoI  = posicaoI - 1
        posicaoJ  = posicaoJ - 1
        if posicaoI  >= 0 and posicaoJ >= 0:
            if tabuleiro[posicaoI][posicaoJ] != '0':
                #print "Diagonal superior"
                return 1
        else:
            return 0
#Função que percorre as no sentido horizontal para o lado DIREITO em busca de algum conflito
def verificaHorizontalDireita(tabuleiro, posicaoI, posicaoJ):
    aux = 0
    for aux in range(len(tabuleiro)):
        posicaoJ  = posicaoJ + 1
        if posicaoJ < len(tabuleiro):
            if tabuleiro[posicaoI][posicaoJ] != '0':
                #print "Horizontal direita"
                return 1
        else:
            return 0

#Função que percorre as casas no sentido horizontal para o lado ESQUERDO em busca de algum conflito
def verificaHorizontalEsquerda(tabuleiro, posicaoI, posicaoJ):
    aux = 0
    for aux in range(len(tabuleiro)):
        posicaoJ  = posicaoJ - 1
        if posicaoJ >= 0:
            if tabuleiro[posicaoI][posicaoJ] != '0':
                #print "horizontal esquerda"
                return 1
        else:
            return 0
#Função que percorre as casas no sentido vertical inferior em busca de algum conflito
def verificaVerticalInferior(tabuleiro, posicaoI, posicaoJ):
    aux = 0
    for aux in range(len(tabuleiro)):
        posicaoI  = posicaoI + 1
        if posicaoI < len(tabuleiro):
            if tabuleiro[posicaoI][posicaoJ] != '0':
                #print "Veritical inferior"
                return 1
        else:
            return 0

#Função que percorre as casas no sentido vertical superior em busca de algum conflito
def verificaVerticalSuperior(tabuleiro, posicaoI, posicaoJ):
    aux = 0
    for aux in range(len(tabuleiro)):
        posicaoI  = posicaoI - 1
        if posicaoI >= 0:
            if tabuleiro[posicaoI][posicaoJ] != '0':
                #print "vertical superior"
                return 1
        else:
            return 0
def getTotalAtackTabuleiro(tabuleiro):
    listaRainhas = getPosicoesElentoMatriz(tabuleiro, '1')
    total = 0
    for rainha in listaRainhas:
        valores = rainha.split(' ')
        posicaoI = int(valores[0])
        posicaoJ = int(valores[1])
        total += getAtackRainha(tabuleiro, posicaoI, posicaoJ)
    return total / 2

# Cria Lista de prioriade com as matrizes oriundas do movimento com a rainha
def listaTabuleiroMovimentosPossiveis(tabuleiro):
    listaNovosTabuleiros = []
    i = 0
    j = 0
    for i in range(0, len(tabuleiro)):
        linha = tabuleiro[i]
        for j in range(0, len(linha)):
            #Percorre a coluna
            matriz = []
            matriz = copy.deepcopy(tabuleiro)
            if  tabuleiro[j][i] != '1':
                posicaAntigaRainha = posicaoElementoColunaMatriz(matriz, '1', i)
                #troca a rainha de lugar
                matriz[posicaAntigaRainha][i] = '0'
                matriz[j][i] = '1'
                heappush(listaNovosTabuleiros, (getTotalAtackTabuleiro(matriz), matriz))
    return listaNovosTabuleiros


#Função que retorna o total de ataques que determinada rainha está oferecendo as outras peças
def getAtackRainha(tabuleiro, posicaoI, posicaoJ):
    total = 0
    total += verificaDiagonalSecundariaInferior(tabuleiro, posicaoI, posicaoJ)
    total += verificaDiagonalSecundariaSuperior(tabuleiro, posicaoI, posicaoJ)
    total += verificaDiagonalPrincipalSuperior(tabuleiro, posicaoI, posicaoJ)
    total += verificaDiagonalPrincipalInferior(tabuleiro, posicaoI, posicaoJ)
    total += verificaHorizontalEsquerda(tabuleiro, posicaoI, posicaoJ)
    total += verificaHorizontalDireita(tabuleiro, posicaoI, posicaoJ)
    total += verificaVerticalInferior(tabuleiro, posicaoI, posicaoJ)
    total += verificaVerticalSuperior(tabuleiro, posicaoI, posicaoJ)
    return total ;

def imprimeMatriz(matriz):
    for i in range(len(matriz)):
        linha = matriz[i]
        print linha
