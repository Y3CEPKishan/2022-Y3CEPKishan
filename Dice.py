import random 


class Dice:
    
    def __init__(self):
        self.num = random.randint(1,6)
        dice1 = '''
         _________
        |         |
        |         | 
        |    O    | 
        |         | 
        |         | 
        \_________/ 
        '''
        dice2 = '''
         _________
        | O       |
        |         | 
        |         | 
        |         | 
        |       O | 
        \_________/ 
        '''
        dice3 ='''
         _________
        | O       |
        |         | 
        |    O    | 
        |         | 
        |       O | 
        \_________/ 
        '''
        dice4 = '''
         _________
        | O     O |
        |         | 
        |         | 
        |         | 
        | O     O | 
        \_________/ 
        '''
        dice5 = '''
         _________
        | O     O |
        |         | 
        |    O    | 
        |         | 
        | O     O | 
        \_________/ 
        '''
        dice6 = '''
         _________
        | O     O |
        |         | 
        | O     O | 
        |         | 
        | O     O | 
        \_________/ 
        '''
        if self.num == 1:
            self.face = dice1
        if self.num == 2:
            self.face = dice2
        if self.num == 3:
            self.face = dice3
        if self.num == 4:
            self.face = dice4
        if self.num == 5:
            self.face = dice5
        if self.num == 6:
            self.face = dice6
    
    def diceNum(self):
        return self.num
        
    def __str__(self):
        return self.face










    
    
    
