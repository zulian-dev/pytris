# -*- coding: utf-8 -*-
#!/usr/bin/env python


class terminal:
    def __init__(self):
        import os
        import platform
        
        if platform.system() == 'Linux':
            clear = 'clear'
        else:
            clear = 'cls'
        
        # se nao limpar o terminal buga todo
        os.system(clear)
        
        
        self.colors = {
            'BLACK'     : '\033[30m',
            'RED'       : '\033[31m',
            'GREEN'     : '\033[32m',
            'YELLOW'    : '\033[33m',
            'BLUE'      : '\033[34m',
            'MAGENTA'   : '\033[35m',
            'CYAN'      : '\033[36m',
            'WHITE'     : '\033[37m',
            
            'BLACKBG'   : '\033[40m',
            'REDBG'     : '\033[41m',
            'GREENBG'   : '\033[42m',
            'YELLOWBG'  : '\033[43m',
            'BLUEBG'    : '\033[44m',
            'MAGENTABG' : '\033[45m',
            'CYANBG'    : '\033[46m',
            'WHITEBG'   : '\033[47m',
            
            'RESET'     : '\033[0m' ,
            'BOLD'      : '\033[1m' ,
            'REVERSE'   : '\033[2m'  
        }
    
    
    '''
        print string
    '''
    def print(self,text):
        print(text)
    
    
    '''
        print char 
    '''
    def printChar(self,char):
        print(self.colors[char.upper()])
    
    
    
    '''
        print char 
    '''
    def printXY(self, text, x, y):
        self.move(x, y)
        self.print(text)
    
    
    '''
        set color to string
    '''
    def setColor(self, text, color):
        return self.colors[color.upper()] + text + self.colors['RESET']
    
    
    '''
        Move cursor to new_x, new_y
    '''
    def move(self,new_x, new_y):
        print ('\033[' + str(new_x) + ';' + str(new_y) + 'H')
    
    
    '''
        Move cursor up # of lines
    '''
    def moveUp(self,lines):
        print ('\033[' + str(lines) + 'A')
    
    
    '''
        Move cursor down # of lines
    '''
    def moveDown(self,lines):
        print ('\033[' + str(lines) + 'B')
    
    
    '''
        Move cursor forward # of chars
    '''
    def moveForward(self,chars):
        print ('\033[' + str(chars) + 'C')
    
    
    '''
        Move cursor backward # of chars
    '''
    def moveBack(self,chars):
        print ('\033[' + str(chars) + 'D')
    
    
    '''
        Saves cursor position
    '''
    def save(self,):
        print ('\033[s')
    
    
    '''
        Restores cursor position
    '''
    def restore(self,):
        print ('\033[u')
    
    
    '''
        Clears screen and homes cursor
    '''
    def clear(self,):
        print ('\033[2J')
    
    
    '''
        Clears screen to end of line
    '''
    def clrtoeol(self,):
        print ('\033[K')
    
    


