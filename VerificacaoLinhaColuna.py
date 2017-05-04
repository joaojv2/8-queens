#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:28:13 2017

@author: joao
"""

class VerificacaoLinhaColuna(object):
    def __init__(self):
        self.total = 0
    
    def verificacaoColuna(self , tabuleiro , linha , coluna):
        for i in range(8):
            if i != linha:
                if tabuleiro.linha[i][coluna] == 1:
                    self.total += 1
        return self.total
                
        
        