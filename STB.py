
class STB:

    def __init__(self):
        self.usednum = []
        self.leftnum = [1,2,3,4,5,6,7,8,9]

    def diceRoll(self, num):
        self.roll = num
        check = 0
        for i in self.leftnum:
            self.leftnum.remove(i)
            if (self.roll - i) in self.leftnum or self.roll - i == 0:
                check = 1
            self.leftnum.append(i)
        if check == 0:
            return 'Game Over'
        elif len(self.leftnum) == 0:
            return 'You Win'
        else:
            return 'cont'

    def pickNum(self, num1, num2 = 0):
        if num1 in self.leftnum:
            if num2 in self.leftnum or num2 == 0:
                if num1 + num2 != self.roll:
                    return 'adderr'
                elif num2 == num1:
                    self.leftnum.remove(num1)
                    self.usednum.append(num1)
                    return 'cont'
                elif num2 == 0:
                    self.leftnum.remove(num1)
                    self.usednum.append(num1)
                    return 'cont'
                else:
                    self.leftnum.remove(num1)
                    self.leftnum.remove(num2)
                    self.usednum.append(num1)
                    self.usednum.append(num2)
                    return 'cont'
            else:
                return 'n2err'
        else:
            return 'n1err'

    def printGame(self):
        board = '''
 _____  _____  _____  _____  _____  _____  _____  _____  _____ 
|     ||     ||     ||     ||     ||     ||     ||     ||     |
|     ||     ||     ||     ||     ||     ||     ||     ||     |
|  1  ||  2  ||  3  ||  4  ||  5  ||  6  ||  7  ||  8  ||  9  |
|     ||     ||     ||     ||     ||     ||     ||     ||     |
|_____||_____||_____||_____||_____||_____||_____||_____||_____|
'''
        fill = ' _____ '
        for e in self.usednum:
            index1 = ((e - 1) * 7) + 1
            for i in range(4):
                board = board[:index1 + 64*i] + ' ' * 7 + board[64*i + index1 + 7:]
            board = board[:index1 + 64*4] + fill + board[64*4 + index1 + 7:]
#           if e == 1:                              unused
#                board = board[0] + board[2:]       code
        return board
            
                
            
        
