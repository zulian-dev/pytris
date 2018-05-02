from pprint import pprint 
from random import randint
from terminal import terminal
import time, os, sys, msvcrt, _thread, multiprocessing, time



keyBoard = {
    "arrow_left"    : b'K' , 
    "arrow_up"      : b'H' , 
    "arrow_right"   : b'M' , 
    "arrow_down"    : b'P' 
}
'''
keyBoard_name_key = {
}

keyBoard_key_name = {

}
'''


class gamepy:
    def __init__(self,):
        
        
        self.keys = {}
        self.declaredKeys = []
        #inicia o teblaco
        
        self.keyBoard_key_name = {}
        self.keyBoard_name_key = {}
        
        self.prepareKeyboard()
        
        
        _thread.start_new_thread( self.teclado, () )
    
    
    def prepareKeyboard(self,):
        for name in keyBoard:
            print(name)
            key = keyBoard[name]
            print(key)
            self.keyBoard_key_name[key] = name
            self.keyBoard_name_key[name] = key
            
            
        
        pprint(self.keyBoard_key_name)
        pprint(self.keyBoard_name_key)
        
        
    
    
    def teclado(self,):
        while True:
            
            key = msvcrt.getch()
            
            print(key)
            
            if key == b'\x03':
                quit()
                
            if key in self.declaredKeys:
                name = self.keyBoard_key_name[key]
                
                self.keys[name]()
                
    
    def setComands(self, obj):
        self.keys = obj
        
        for nameKey in obj:
            numberKey = self.keyBoard_name_key[nameKey]
            self.declaredKeys.append(numberKey)
            
            
        
        
        
    def clock(self,):
        while True:
            print('cloclou')
            # input('?')
            time.sleep(1)
    
    

