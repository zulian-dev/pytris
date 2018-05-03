from pprint import pprint 
from random import randint
from terminal import terminal
import time, os, sys, msvcrt, _thread, multiprocessing, time



keyBoard = {
    "arrow_left"    : b'K'   , 
    "arrow_up"      : b'H'   , 
    "arrow_right"   : b'M'   , 
    "arrow_down"    : b'P'   , 
    "esc"           : b'\x03'  
}


'''
keyBoard_name_key = {
}

keyBoard_key_name = {

}
'''


class gamepy:
    def __init__(self,):
        
        self.X = -1 # colunas
        self.Y = -1 # linhas
        # self.Z = -1 # profundidadde
        self.Z = [] # profundidadde
        
        
        self.matrix=[]
        
        self.blank = '  '
        
        
        #inicia o teclado 
        self.keys = {}              # 
        self.declaredKeys = []      # 
        self.keyBoard_key_name = {} # 
        self.keyBoard_name_key = {} # 
        
        self.prepareKeyboard()
        
        
    def prepareKeyboard(self,):
        for name in keyBoard:
            key = keyBoard[name]
            self.keyBoard_key_name[key] = name
            self.keyBoard_name_key[name] = key
        _thread.start_new_thread(self.teclado, ())
    
    
    def teclado(self,):
        while True:
            key = msvcrt.getch()
            if key in self.declaredKeys:
                name = self.keyBoard_key_name[key]
                self.keys[name]()
                
            
        
    
    def setComands(self, obj):
        self.keys = obj
        
        for nameKey in obj:
            numberKey = self.keyBoard_name_key[nameKey]
            self.declaredKeys.append(numberKey)
            
        
    
    
    
    
    
    
    
    
    def setMatrix(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z
    
    def setBorder(self, hasBorder):
        self.hasBorder = hasBorder
    
    def createMatrix(self, ):
        for y in range(0, self.Y):
            self.matrix[y] = {}
            for x in range(0, self.X):
                # if x == 0 or x == self.X-1 or y == self.Y-1:
                self.matrix[y][x] = self.blank
                
    
    
    def render (self):
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
        

    
    
    
    
    
    
    
    
    
    
    
    
    def clock(self,):
        while True:
            
            time.sleep(1)
            
        
    
    
    def start(self,):
        self.clock()
    

