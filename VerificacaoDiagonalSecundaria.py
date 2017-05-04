#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:28:13 2017

@author: joao
"""

class VerificaDiagonalSecundaria(object):
    def __init__(self):
        self.total = 0
    
    def verificarDiagonalSecundariaInferior (self , tabuleiro , linha , coluna):
        if coluna > 0:
            linha = linha + 1
            coluna = coluna - 1
            while coluna >= 0:
                if linha > 7:
                    break
                if tabuleiro.linha[linha][coluna] == 1:
                   self.total += 1
                coluna -= 1 
                linha += 1
            return self.total
        else:
            return self.total
    
    def verificarDiagonalSecundariaSuperior (self , tabuleiro , linha , coluna):
        if coluna < 7:
            linha = linha - 1
            coluna = coluna + 1
            while coluna < 7:
                if linha < 0:
                    break
                if tabuleiro.linha[linha][coluna] == 1:
                    self.total += 1
                linha -= 1 
                coluna += 1
            return self.total
        else:
            return self.total