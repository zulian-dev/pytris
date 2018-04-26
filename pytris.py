#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pprint import pprint 
from random import randint
from terminal import terminal
import time, os, sys, msvcrt, _thread, multiprocessing, time

class pytrix:
    
    def __init__(self):
        
        self.X=20
        self.Y=20
        
        self.px = 0
        self.py = 0
        self.pt = ''
        
        self.bg = {}
        self.pc = {}
        
        self.P = 0
        
        self.terminal = terminal()
        
        self.brick  = u'█'*2 
        
        self.wall  = self.terminal.setColor(self.brick, 'Cyan'  ) 
        self.blank = self.terminal.setColor(self.brick, 'Black' ) 
        
        self.pices = {
            'O' : {
                'up':{
                    0:[0,1],
                    1:[0,1]
                },
                'color':"Red"
            }, 
            'I' : {
                'up':{
                    0:[0],
                    1:[0],
                    2:[0],
                    3:[0]
                },
                'color':"Green"
            },
            'L' : {
                'up':{
                    0:[0],
                    1:[0],
                    2:[0,1],
                },
                'color':"Yellow"
            },
            'Z' : {
                'up':{
                    0:[0,1],
                    1:[1,2]
                },
                'color':"Blue"
            },
            'S' : {
                'up':{
                    0:[2,3],
                    1:[1,2]
                },
                'color':"Magenta"
            },
            'T' : {
                'up':{
                    0:[1,2,3],
                    1:[2]
                },
                'color':"White"
            }
            
            #'long'   :  ,
            #'Z'      : '' ,
        }
        
        
        
        
        self.startCene()
        self.novaPeca()
        
        #teclado = myThread(1, "Thread1", self)
        #teclado.start()
        _thread.start_new_thread( self.teclado, () )
        
    def clear(self):
        # print ('\033[' + str(0) + ';' + str(0) + 'H')
        os.system('cls')
    
    
    def teclado(self):
        while True:
            
            key = msvcrt.getch()
            
            if key == b'K':
                self.px-=1
                self.renderPice()
                self.render()
            
            elif key == b'M':
                self.px+=1
                self.renderPice()
                self.render()
            
            elif key == b'\x1b':
                quit()


    
    
    def startCene(self):
        for y in range(0,self.Y):
            self.bg[y] = {} 
            self.pc[y] = {} 
            for x in range(0, self.X):
                if x == 0 or x == self.X-1 or y == self.Y-1:
                    self.bg[y][x] = self.wall
                    self.pc[y][x] = self.blank
                else:
                    self.pc[y][x] = self.blank
                    self.bg[y][x] = self.blank
                
            
        
    
    def render(self):
        cenario=''
        cenario+=("\n")
        
        for y in range(0, self.Y):
            for x in range(0, self.X):
                
                if self.pc[y][x] != self.blank:
                    cenario+=self.pc[y][x]
                    self.pc[y][x] = self.blank
                else:
                    cenario+=self.bg[y][x]
                
            cenario+=("\n")
        
        cenario+=("Pontos: " + str(self.P))
        
        self.terminal.printXY(cenario, 0, 0)
        # self.clear()
        #print(cenario)
        # print ("\x1b[31;4mHello\x1b[0m")
        
        # print ('A')
        
        
        
        
    def calcNext(self):
        self.py+=1
        self.renderPice()
    
    def renderPice(self):
        
        if self.px == 0 and self.py == 0:
            return
        
        pice = self.pices[self.pt]
        
        for linha in pice['up']:
            for pedaco in pice['up'][linha]:
                if self.bg[self.py+linha][self.px+pedaco] == self.blank:
                    #self.pc[self.py+linha][self.px+pedaco] = pice['color'] + self.brick + bcolors.ENDC
                    self.pc[self.py+linha][self.px+pedaco] = self.terminal.setColor(self.brick, pice['color']) 
                else:
                    for linha in pice['up']:
                        for pedaco in pice['up'][linha]:
                            #self.bg[self.py+linha-1][self.px+pedaco] = pice['color'] + self.brick + bcolors.ENDC
                            self.bg[self.py+linha-1][self.px+pedaco] = self.terminal.setColor(self.brick, pice['color']) 
                    
                    self.verifyPontos()
                    self.novaPeca()
                
            
        
    
    def novaPeca(self):
        pices = ['O','I','L','Z','S','T']
        
        self.pt =pices[ randint(0, len(pices)-1) ]
        
        
        self.px = int(self.X / 2)
        
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
                    
                
        
    
    def getKey(self):
        import msvcrt
        key = msvcrt.getch()
        
        if key == b'K':
            self.px-=1
        
        elif key == b'M':
            self.px+=1
        
        
        pass
        
    
    def clock(self):
        #clock = 0
        while True:
            #self.clear()
            # self.getKey()
            self.render()
            #self.verifyPontos()
            self.calcNext()
            #input('?')
            time.sleep(.6)
            



g = pytrix()
g.clock()




