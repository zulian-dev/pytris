


from gamepy import gamepy 


class sneaky(gamepy):
    def __init__(self):
        super(sneaky, self).__init__()
        
        self.setComands({
            "arrow_left"  : lambda *x : self.left(),
            "arrow_up"    : lambda *x : self.up(),
            "arrow_right" : lambda *x : self.right(),
            "arrow_down"  : lambda *x : self.down()
        })
        
        self.clock()
        
    def up(self,):
        print('UP')
        
    def right(self,):
        print('RIGHT')
        
    def left(self,):
        print('LEFT')
        
    def down(self,):
        print('DOWN')
        
        
if __name__ == '__main__':
    c = sneaky()
    
    