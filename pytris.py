#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint 
import time
import os

from random import randint




class pytrix:
    
    def __init__(self):
        
        self.X=20
        self.Y=20
        
        """ self.X=10
        self.Y=10 """
        
        self.px = 0
        self.py = 0
        
        self.bg = {}
        self.pc = {}
        
        self.P = 0
        
        
        
        self.wall   = u'█'*2
        self.brick  = u'▓'*2
        self.blank  = u'░'*2
        
        pices = {
            'squere' : '' ,
            'long'   : '' ,
            'Z'      : '' ,
        }
        
        
        
        
        self.startCene()
        self.novaPeca()
        
        
    def clear(self):
        os.system('cls')
    
    
    def startCene(self):
        for y in range(0,self.Y):
            self.bg[y] = {} 
            for x in range(0, self.X):
                if x == 0 or x == self.X-1 or y == self.Y-1:
                    self.bg[y][x] = self.wall
                else:
                    self.bg[y][x] = self.blank
                
            
        
    
    def render(self):
        cenario=''
        for y in range(0, self.Y):
            for x in range(0, self.X):
                cenario+=(self.bg[y][x])
            cenario+=("\n")
            
        cenario+=("Pontos: " + str(self.P))
        
        print(cenario)
        
        
        
    def calcNext(self):
        
        if self.px == 0 and self.py == 0:
            return
        
        self.py+=1
        
        if self.bg[self.py][self.px] == self.blank:
            self.bg[self.py-1][self.px] = self.blank
            #self.bg[self.py][self.px] = '@@'
            self.bg[self.py][self.px] = self.brick
        else:
            self.verifyPontos()
            self.novaPeca()
        
        
        
    def novaPeca(self):
        self.px = randint(1, self.X-1)
        self.py = 0
        
    
    
    
    
    def verifyPontos(self):
        
        for y in range(0, self.Y-1):
            ponto=True
            for x in range(0, self.X):
                if x == 0 or x == self.X-1 or y == self.Y-1:
                    pass
                else:
                    if self.bg[y][x] == self.blank:
                        ponto=False
                    
            if ponto:
                self.P += 1
                for x in range(0, self.X):
                    self.bg[y][x] = self.blank
                    
                
                yy = y
                
                while (yy!=0):
                    self.bg[yy] = self.bg[yy-1]
                    yy-=1
                    
                
            
        
    
    def clock(self):
        #clock = 0
        while True:
            self.clear()
            self.render()
            #self.verifyPontos()
            self.calcNext()
            #input('?')
            time.sleep(.6)


g = pytrix()

g.clock()






