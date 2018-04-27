#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pprint import pprint 
from random import randint
from terminal import terminal
import time, os, sys, msvcrt, _thread, multiprocessing, time





keyBoard = {
    "backspace"    :  "8",
    "tab"          :  "9",
    "enter"        : "13",
    "shift"        : "16",
    "ctrl"         : "17",
    "alt"          : "18",
    "pause"        : "19",
    "capslock"     : "20",
    "escape"       : "27",
    "pageup"       : "33",
    "pagedown"     : "34",
    "end"          : "35",
    "home"         : "36",
    "leftarrow"    : "37",
    "uparrow"      : "38",
    "rightarrow"   : "39",
    "downarrow"    : "40",
    "insert"       : "45",
    "delete"       : "46",
    "0"            : "48",
    "1"            : "49",
    "2"            : "50",
    "3"            : "51",
    "4"            : "52",
    "5"            : "53",
    "6"            : "54",
    "7"            : "55",
    "8"            : "56",
    "9"            : "57",
    "a"            : "65",
    "b"            : "66",
    "c"            : "67",
    "d"            : "68",
    "e"            : "69",
    "f"            : "70",
    "g"            : "71",
    "h"            : "72",
    "i"            : "73",
    "j"            : "74",
    "k"            : "75",
    "l"            : "76",
    "m"            : "77",
    "n"            : "78",
    "o"            : "79",
    "p"            : "80",
    "q"            : "81",
    "r"            : "82",
    "s"            : "83",
    "t"            : "84",
    "u"            : "85",
    "v"            : "86",
    "w"            : "87",
    "x"            : "88",
    "y"            : "89",
    "z"            : "90",
    "lwindow"      : "91",
    "rwindow"      : "92",
    "selectkey"    : "93",
    "numpad0"      : "96",
    "numpad1"      : "97",
    "numpad2"      : "98",
    "numpad3"      : "99",
    "numpad4"      : "100",
    "numpad5"      : "101",
    "numpad6"      : "102",
    "numpad7"      : "103",
    "numpad8"      : "104",
    "numpad9"      : "105",
    "multiply"     : "106",
    "add"          : "107",
    "subtract"     : "109",
    "decimalpoint" : "110",
    "divide"       : "111",
    "f1"           : "112",
    "f2"           : "113",
    "f3"           : "114",
    "f4"           : "115",
    "f5"           : "116",
    "f6"           : "117",
    "f7"           : "118",
    "f8"           : "119",
    "f9"           : "120",
    "f10"          : "121",
    "f11"          : "122",
    "f12"          : "123",
    "numlock"      : "144",
    "scrolllock"   : "145",
    "semicolon"    : "186",
    "equalsign"    : "187",
    "comma"        : "188",
    "dash"         : "189",
    "period"       : "190",
    "forwardslash" : "191",
    "graveaccent"  : "192",
    "openbracket"  : "219",
    "backslash"    : "220",
    "closebraket"  : "221"
}





















class gamepy:
    def __init__(self,):
        
        
        #inicia o teblaco
        _thread.start_new_thread( self.teclado, () )
        
    def teclado(self,):
        pass
    
    
    
    


class pytrix:
    
    def __init__(self):
        
        self.X=20
        self.Y=20
        
        self.px = 0
        self.py = 0
        self.pt = ''
        self.ps = ''
        
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
                'right':{
                    1:[-1, 0, 1, 2]
                },
                'down':{
                    0:[0],
                    1:[0],
                    2:[0],
                    3:[0]
                },
                'left':{
                    1:[-1, 0, 1, 2]
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
        }
        
        self.startCene()
        self.novaPeca()
        
        _thread.start_new_thread( self.teclado, () )
        
    
    def teclado(self):
        while True:
            
            key = msvcrt.getch()
            
            if key == b'K':
                self.px-=1
            
            elif key == b'M':
                self.px+=1
            
            elif key == b'H':
                self.rotate()
            
            elif key == b'\x1b':
                quit()
            
            else:
                return 
            
            self.renderPice()
            self.render()
            
        
    
    
    
    
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
        cenario+="\n"
        
        for y in range(0, self.Y):
            for x in range(0, self.X):
                
                if self.pc[y][x] != self.blank:
                    cenario+=self.pc[y][x]
                    self.pc[y][x] = self.blank
                
                else:
                    cenario+=self.bg[y][x]
                
            cenario+=("\n")
        
        cenario += "Pontos: " + str(self.P)
        
        self.terminal.printXY(cenario, 0, 0)
        
        
    def calcNext(self):
        self.py+=1
        self.renderPice()
    
    def renderPice(self):
        
        if self.px == 0 and self.py == 0:
            return
        
        pice = self.pices[self.pt]
        
        for linha in pice[self.ps]:
            for pedaco in pice[self.ps][linha]:
                if self.bg[self.py+linha][self.px+pedaco] == self.blank:
                    #self.pc[self.py+linha][self.px+pedaco] = pice['color'] + self.brick + bcolors.ENDC
                    self.pc[self.py+linha][self.px+pedaco] = self.terminal.setColor(self.brick, pice['color']) 
                else:
                    for linha in pice[self.ps]:
                        for pedaco in pice[self.ps][linha]:
                            #self.bg[self.py+linha-1][self.px+pedaco] = pice['color'] + self.brick + bcolors.ENDC
                            self.bg[self.py+linha-1][self.px+pedaco] = self.terminal.setColor(self.brick, pice['color']) 
                    
                    self.verifyPontos()
                    self.novaPeca()
                
            
        
    
    def rotate(self):
        if self.ps == 'up':
            self.ps = 'right'
        elif self.ps == 'right':
            self.ps = 'down'
        elif self.ps == 'down':
            self.ps = 'left'
        elif self.ps == 'left':
            self.ps = 'up'
    
    
    def novaPeca(self):
        pices = ['O','I','L','Z','S','T']
        
        # self.pt = pices[ randint(0, len(pices)-1) ]
        
        self.pt = 'I'
        
        self.ps = 'up'
        
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
                    
                
        
    
    
    def clock(self):
        while True:
            self.render()
            self.calcNext()
            # input('?')
            time.sleep(.6)
            



g = pytrix()
g.clock()




