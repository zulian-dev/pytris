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
        
        
        self.terminal = terminal()
        
        self.X = -1 # colunas
        self.Y = -1 # linhas
        # self.Z = -1 # profundidadde
        self.Z = {} # profundidadde
        
        
        self.matrix=[]
        
        self.blank = '  '
        self.blank = 'XX'
        
        
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
        for layer in self.Z:
            self.matrix[layer] = {}
            for y in range(0, self.Y):
                self.matrix[layer][y] = {}
                for x in range(0, self.X):
                    self.matrix[layer][y][x] = self.blank
                    
                    # if x == 0 or x == self.X-1 or y == self.Y-1:
                    
                
            
        
    
    def getLayer(self, layer):
        return self.matrix[layer]
    
    
    def editLayer(self,layer):
        pass
    
    
    
    def render (self):
        cenario=''
        cenario+="\n"
        for y in range(0, self.Y):
            for x in range(0, self.X):
                for layer in self.Z:
                    
                    char = str(self.matrix[layer][y][x])
                    
                    peca = self.blank
                    
                    if char != self.blank:
                        peca = char
                    
                    
                    cenario += peca
            cenario += "\n"
        #cenario += "Pontos: " + str()
        self.terminal.printXY(cenario, 0, 0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    def clock(self,):
        
        clocks = 0
        
        while True:
            
            
            self.render()
            
            if (clocks==5):
                quit()
            
            clocks+=1
            
            print(clocks)
            
            time.sleep(1)
            
        
    
    
    def start(self,):
        self.clock()
    

