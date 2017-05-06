#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:28:13 2017

@author: joao
"""
from random import randint

class Mutacao(object):

	def __init__ (self , array1):
		self.array1 = array1

	def Mutacao(self):
		a = randint(0 , 7)
		b = randint(0 , 7)
		c = self.array1[a]
		
		self.array1[a] = self.array1[b]
		self.array1[b] = c

		return self.array1