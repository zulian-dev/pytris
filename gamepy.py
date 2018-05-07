from pprint import pprint 
from random import randint
import time, os, sys, msvcrt, _thread, multiprocessing, time

from terminal import terminal
import keyboard







'''
keyBoard_name_key = {
}

keyBoard_key_name = {

}
'''


class gamepy:
    def __init__(self,):
        
        
        self.terminal = terminal()
        
        
        self.matrix={}
        
        self.X = -1 # colunas
        self.Y = -1 # linhas
        self.Z = {} # profundidadde
        
        self.blank = '  '
        self.brick = u'█'*2 
        
        self.clockTime = 1
        
        
        self.objectsList={}
        self.colisions={}
        
        
        #inicia o teclado 
        self.keys = {}              # 
        self.declaredKeys = []      # 
        self.keyBoard_key_name = {} # 
        self.keyBoard_name_key = {} # 
        
        self.prepareKeyboard()
        
        
    def prepareKeyboard(self,):
        for name in keyboard.keys:
            key = keyboard.keys[name]
            self.keyBoard_key_name[key] = name
            self.keyBoard_name_key[name] = key
        _thread.start_new_thread(self.teclado, ())
    
    
    def teclado(self,):
        while True:
            key = msvcrt.getch()
            print(key)
            
            if key in self.declaredKeys:
                name = self.keyBoard_key_name[key]
                self.keys[name]()
                
            
        
    
    def setComands(self, obj):
        self.keys = obj
        
        for nameKey in obj:
            numberKey = self.keyBoard_name_key[nameKey]
            self.declaredKeys.append(numberKey)
            
        
    def setColision(self, layer1, layer2, fn):
        colisionName1 = str(layer1) + '-' + str(layer2)
        colisionName2 = str(layer2) + '-' + str(layer1)
        self.colisions[colisionName1] = fn
        self.colisions[colisionName2] = fn
    
    
    def setMatrix(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.createMatrix()
    
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
                
                peca = self.blank
                
                for layer in self.Z:
                    char = str(self.matrix[layer][y][x])
                    if char != self.blank:
                        peca = char
                    
                cenario += peca
            cenario += "\n"
        #cenario += "Pontos: " + str()
        self.terminal.printXY(cenario, 0, 0)
    
    
    
    
    
    
    
    
    
    def createObject(self, obj):
        layer = obj['layer']
        #name = obj.name
        self.objectsList[layer] = obj
    
    
    def nextFrame(self):
        
        ocupedX={}
        ocupedY={}
        
        
        for layer in self.objectsList:
            
            if layer in self.matrix:
                self.clearLayer(layer)
                
                objx     = self.objectsList[layer]['X']
                objy     = self.objectsList[layer]['Y']
                objcolor = self.objectsList[layer]['color']
                
                #print(self.setColor('X', objcolor))
                self.matrix[layer][objy][objx] = self.setColor(self.brick, objcolor)
                
                if objx in ocupedX and objy in ocupedY:
                    pass
                else :
                    objx
                    objy
                    ocupedX
                    ocupedY
                
            # self.matrix[layer][y][x]
            
    
    def clearLayer(self, layer):
        for y in range(0, self.Y):
            for x in range(0, self.X):
                self.matrix[layer][y][x] = self.blank
        

    

    def clock(self,):
        
        clocks = 0
        
        while True:
            
            self.nextFrame()
            
            self.render()
            
            if (clocks==10):
                quit()
            
            clocks+=1
            
            print(clocks)
            
            time.sleep(self.clockTime)
            
        
    def setColor(self, text, color):
        return self.terminal.setColor(text, color)
    

    def start(self,):
        self.clock()
    

if __name__ == '__main__':
    engine = gamepy()
    engine.start()
