# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 08:20:37 2019

@author: Lucer
"""

 # -*- coding:utf-8 -*
 
class Ahorcado(object):
    def init (self, no_fallar, palabras)
    self.no_fallar= no_fallar
    self.palabras=palabras 
    self.adivina=[]
    self.gane=False
    self.falla=0
    self.perdi=false
    def jugar(self, letra):
        if letra in self. palabras:
            self.adivina.oppend(letra)
        else:
            gane=False
            for letra in self.palabra:
                if letra not on self.adivina:
                    gane=False 
                    if gane:
                        self.gane=True
            self.falle +1
            if self.falle>= self.no_fallar:
                self.perdi=True
                self.estado()
                        
                        
            
            