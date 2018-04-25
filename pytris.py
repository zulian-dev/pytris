#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint 
import time
import os
import sys

from random import randint


class bcolors:
    Black="\033[0;30m"        # Black
    Red="\033[0;31m"          # Red
    Green="\033[0;32m"        # Green
    Yellow="\033[0;33m"       # Yellow
    Blue="\033[0;34m"         # Blue
    Purple="\033[0;35m"       # Purple
    Cyan="\033[0;36m"         # Cyan
    White="\033[0;37m"        # White

    # Bold
    BBlack="\033[1;30m"       # Black
    BRed="\033[1;31m"         # Red
    BGreen="\033[1;32m"       # Green
    BYellow="\033[1;33m"      # Yellow
    BBlue="\033[1;34m"        # Blue
    BPurple="\033[1;35m"      # Purple
    BCyan="\033[1;36m"        # Cyan
    BWhite="\033[1;37m"       # White

    # Underline
    UBlack="\033[4;30m"       # Black
    URed="\033[4;31m"         # Red
    UGreen="\033[4;32m"       # Green
    UYellow="\033[4;33m"      # Yellow
    UBlue="\033[4;34m"        # Blue
    UPurple="\033[4;35m"      # Purple
    UCyan="\033[4;36m"        # Cyan
    UWhite="\033[4;37m"       # White

    # Background
    On_Black="\033[40m"       # Black
    On_Red="\033[41m"         # Red
    On_Green="\033[42m"       # Green
    On_Yellow="\033[43m"      # Yellow
    On_Blue="\033[44m"        # Blue
    On_Purple="\033[45m"      # Purple
    On_Cyan="\033[46m"        # Cyan
    On_White="\033[47m"       # White

    # High Intensty
    IBlack="\033[0;90m"       # Black
    IRed="\033[0;91m"         # Red
    IGreen="\033[0;92m"       # Green
    IYellow="\033[0;93m"      # Yellow
    IBlue="\033[0;94m"        # Blue
    IPurple="\033[0;95m"      # Purple
    ICyan="\033[0;96m"        # Cyan
    IWhite="\033[0;97m"       # White

    # Bold High Intensty
    BIBlack="\033[1;90m"      # Black
    BIRed="\033[1;91m"        # Red
    BIGreen="\033[1;92m"      # Green
    BIYellow="\033[1;93m"     # Yellow
    BIBlue="\033[1;94m"       # Blue
    BIPurple="\033[1;95m"     # Purple
    BICyan="\033[1;96m"       # Cyan
    BIWhite="\033[1;97m"      # White

    # High Intensty backgrounds
    On_IBlack="\033[0;100m"   # Black
    On_IRed="\033[0;101m"     # Red
    On_IGreen="\033[0;102m"   # Green
    On_IYellow="\033[0;103m"  # Yellow
    On_IBlue="\033[0;104m"    # Blue
    On_IPurple="\033[10;95m"  # Purple
    On_ICyan="\033[0;106m"    # Cyan
    On_IWhite="\033[0;107m"   # White
    
    ENDC = '\033[0m'


















class pytrix:
    
    def __init__(self):
        
        self.X=20
        self.Y=20
        
        """ self.X=10
        self.Y=10 """
        
        self.px = 0
        self.py = 0
        self.pt = ''
        
        self.bg = {}
        self.pc = {}
        
        self.P = 0
        
        self.brick  = u'█'*2 
        self.wall   = bcolors.Cyan +  u'█'*2 + bcolors.ENDC
        self.blank  = bcolors.Black +  u'█'*2 + bcolors.ENDC
        
        self.pices = {
            #'squere' : [[0,1], [0,1]] 
            'O' : {
                'up':{
                    0:[0,1],
                    1:[0,1]
                },
                'color':bcolors.Red
            }, 
            'I' : {
                'up':{
                    0:[0],
                    1:[0],
                    2:[0],
                    3:[0]
                },
                'color':bcolors.Green
            },
            'L' : {
                'up':{
                    0:[0],
                    1:[0],
                    2:[0,1],
                },
                'color':bcolors.Yellow
            },
            'Z' : {
                'up':{
                    0:[0,1],
                    1:[1,2]
                },
                'color':bcolors.Blue
            },
            'S' : {
                'up':{
                    0:[2,3],
                    1:[1,2]
                },
                'color':bcolors.Purple
            },
            'T' : {
                'up':{
                    0:[1,2,3],
                    1:[2]
                },
                'color':bcolors.White
            }
            
            #'long'   :  ,
            #'Z'      : '' ,
        }
        
        
        
        
        self.startCene()
        self.novaPeca()
        
        
    def clear(self):
        os.system('cls')
    
    
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
        self.clear()
        print(cenario)
        
        
        
    def calcNext(self):
        
        if self.px == 0 and self.py == 0:
            return
        
        self.py+=1
        
        pice = self.pices[self.pt]
        
        for linha in pice['up']:
            for pedaco in pice['up'][linha]:
                if self.bg[self.py+linha][self.px+pedaco] == self.blank:
                    self.pc[self.py+linha][self.px+pedaco] = pice['color'] + self.brick + bcolors.ENDC
                else:
                    self.verifyPontos()
                    self.novaPeca()
        
        '''
        if self.bg[self.py][self.px] == self.blank:
            self.bg[self.py-1][self.px] = self.blank
            self.bg[self.py][self.px] = self.brick
        else:
            self.verifyPontos()
            self.novaPeca()
        '''
        
        
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
        # key = sys.stdin.readline()
        # print(key)
        pass
        
        
    
    def clock(self):
        #clock = 0
        while True:
            #self.clear()
            self.getKey()
            # self.render()
            #self.verifyPontos()
            self.calcNext()
            #input('?')
            time.sleep(.6)
            



g = pytrix()
g.clock()




