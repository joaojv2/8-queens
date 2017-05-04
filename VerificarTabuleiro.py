#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:28:13 2017

@author: joao
"""

from VerificacaoLinhaColuna import VerificacaoLinhaColuna
from VerificacaoDiagonalPrincipal import VerificaDiagonalPrincipal
from VerificacaoDiagonalSecundaria import VerificaDiagonalSecundaria

class VerificarTabuleiro(object):
    def __init__(self , tabuleiro , fitness):
            self.tabuleiro = tabuleiro
            self.fitness = fitness
            
    def verificarTabuleiro (self):
        for i in range(8):
                for j in range(8):
                    if self.tabuleiro.linha[i][j] == 1:
                        self.fitness += VerificacaoLinhaColuna().verificacaoColuna(self.tabuleiro , i , j)
                        self.fitness += VerificaDiagonalPrincipal().verificarDiagonalPrincipalInferior(self.tabuleiro , i , j)
                        self.fitness += VerificaDiagonalPrincipal().verificarDiagonalPrincipalSuperior(self.tabuleiro , i , j)
                        self.fitness += VerificaDiagonalSecundaria().verificarDiagonalSecundariaInferior(self.tabuleiro , i , j)
                        self.fitness += VerificaDiagonalSecundaria().verificarDiagonalSecundariaSuperior(self.tabuleiro , i , j)
        return self.fitness                