


from gamepy import gamepy 


class sneaky(gamepy):
    def __init__(self):
        super(sneaky, self).__init__()
        
        
        self.blank = self.setColor(u'█'*2, 'white')
        
        self.setComands({
            "arrow_left"  : lambda *x : self.left(),
            "arrow_up"    : lambda *x : self.up(),
            "arrow_right" : lambda *x : self.right(),
            "arrow_down"  : lambda *x : self.down(),
            "esc"         : lambda *x : self.esc()
        })
        
        self.setMatrix(20, 20, ['bg', 'comida', 'cobra'])
        
        self.setBorder(True)
        
        self.clockTime = .2
        
        
        self.createObjs()
        
        
    def up(self,):
        print('UP')
        
    def right(self,):
        print('RIGHT')
        
    def left(self,):
        print('LEFT')
        
    def down(self,):
        print('DOWN')
        
    def esc(self,):
        import sys
        sys.exit()
        
    def createObjs(self):
        # cobra 
        self.createObject({ 
            'X':5,
            'Y':5,
            'color':'red',
            'layer': 'cobra'
        })
        
        #comida
        self.createObject({ 
            'X':10,
            'Y':5,
            'color':'blue',
            'layer': 'comida'
        })
        
        self.setColision('cobra', 'comida', lambda *x: self.comer())
        
    def comer(self):
        print ('comeu')
        
    def nextFrame(self):
        
        self.objectsList['cobra']['X'] += 1
        
        super(sneaky, self).nextFrame()
        
        
if __name__ == '__main__':
    c = sneaky()
    c.start()
    
    
