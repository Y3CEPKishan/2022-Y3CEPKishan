
class SL:

    def __init__(self):
        # symbol representing each player
        
        self.player1 = '\u2660'
        self.player2 = '\u2663'
        self.player3 = '\u2665'
        self.player4 = '\u2666'
        # starting each player at 0
        
        self.pos1 = 0
        self.pos2 = 0
        self.pos3 = 0
        self.pos4 = 0

    def playeradd(self,player,roll):

        # the entrances and exits to snakes and ladders
        
        entrances = [1,16,34,31,26,46,49,78,64,54,90,96,82]
        exits = [26,4,8,11,43,40,32,60,75,88,92,57,100]
        if player == 1:
            self.pos1 += roll
        elif player == 2:
            self.pos2 += roll
        elif player == 3:
            self.pos3 += roll
        elif player == 4:
            self.pos4 += roll
        else:
            self.pos4 += roll

        # if a player is at an entrace of a snake or ladder
        # move them to the exit

        for i,e in enumerate(entrances):
            if self.pos1 == e:
                self.pos1 = exits[i]
            if self.pos2 == e:
                self.pos2 = exits[i]
            if self.pos3 == e:
                self.pos3 = exits[i]
            if self.pos4 == e:
                self.pos4 = exits[i]
                
        # determining if theres a winner
                
        if self.pos1 >= 100:
            return 'win1'
        elif self.pos2 >= 100:
            return 'win2'
        elif self.pos3 >= 100:
            return 'win3'
        elif self.pos4 >= 100:
            return 'win4'
        else:
            return 'cont'
    def printBoard(self):

        # a board containing the player positions
        
        board = '''
     _________________________________________________                           
    |100#|99  |98  |97  |96# |95  |94  |93  |92# |91  |                          
    |    |    |    |    |    |    |    |    |    |    |<-                        
    |____|____|____|____|____|____|____|____|____|____|  |                       
    |81  |82# |83  |84  |85  |86  |87  |88# |89  |90# |  |                       
  ->|    |    |    |    |    |    |    |    |    |    |--                        
 |  |____|____|____|____|____|____|____|____|____|____|                          
 |  |80  |79  |78# |77  |76  |75# |74  |73  |72  |71  |                          
  --|    |    |    |    |    |    |    |    |    |    |<-                        
    |____|____|____|____|____|____|____|____|____|____|  |                       
    |61  |62  |63  |64# |65  |66  |67  |68  |69  |70  |  |                       
  ->|    |    |    |    |    |    |    |    |    |    |--                        
 |  |____|____|____|____|____|____|____|____|____|____|                          
 |  |60# |59  |58  |57# |56  |55  |54# |53  |52  |51  |                          
  --|    |    |    |    |    |    |    |    |    |    |<-                        
    |____|____|____|____|____|____|____|____|____|____|  |                       
    |41  |42  |43# |44  |45  |46# |47  |48  |49# |50  |  |                       
  ->|    |    |    |    |    |    |    |    |    |    |--                        
 |  |____|____|____|____|____|____|____|____|____|____|                          
 |  |40# |39  |38  |37  |36  |35  |34# |33  |32# |31# |                          
  --|    |    |    |    |    |    |    |    |    |    |<-                        
    |____|____|____|____|____|____|____|____|____|____|  |                       
    |21  |22  |23  |24  |25  |26# |27  |28  |29  |30  |  |                       
  ->|    |    |    |    |    |    |    |    |    |    |--                        
 |  |____|____|____|____|____|____|____|____|____|____|                          
 |  |20  |19  |18  |17  |16# |15  |14  |13  |12  |11# |                          
  --|    |    |    |    |    |    |    |    |    |    |<-                        
    |____|____|____|____|____|____|____|____|____|____|  |                       
    |1#  |2   |3   |4#  |5   |6   |7   |8#  |9   |10  |  |                       
    |    |    |    |    |    |    |    |    |    |    |--                        
    |____|____|____|____|____|____|____|____|____|____|                          

 ________
|        |
|1  -> 26|
|4  <- 16|
|8  <- 34|
|11 <- 31|
|26 -> 43|
|40 <- 46|
|32 <- 49|
|60 <- 78|
|64 -> 75|
|54 -> 88|
|90 -> 92|
|57 <- 96|
|82 ->100|
|________|
'''

        # calculating each player's position on the board in terms of string index
        # each player symbol cannnot overlap each other on the map
        # thus the index has to be calculated for each player]
        
        if self.pos1 != 0 and self.pos1 < 100:
            if ((self.pos1 - 1)//10)%2 == 0:
                horizontal = (self.pos1 - 1) % 10
                vertical = (self.pos1 - 1) // 10
            else:
                horizontal = 9 - ((self.pos1 - 1) % 10)
                vertical = (self.pos1 - 1) // 10
            index = (88 + 28 * 82) + (horizontal * 5) - (vertical * 82 * 3)
            board = board[:index] + self.player1 + board[index + 1:]
            
        if self.pos2 != 0 and self.pos2 < 100:
            if ((self.pos2 - 1)//10)%2 == 0:
                horizontal = (self.pos2 - 1) % 10
                vertical = (self.pos2 - 1) // 10
            else:
                horizontal = 9 - ((self.pos2 - 1) % 10)
                vertical = (self.pos2 - 1) // 10
            index = (88 + 28 * 82) + (horizontal * 5) - (vertical * 82 * 3) + 1
            board = board[:index] + self.player2 + board[index + 1:]
            
        if self.pos3 != 0 and self.pos3 < 100:
            if ((self.pos1 - 1)//10)%2 == 0:
                horizontal = (self.pos3 - 1) % 10
                vertical = (self.pos3 - 1) // 10
            else:
                horizontal = 9 - ((self.pos3 - 1) % 10)
                vertical = (self.pos3 - 1) // 10
            index = (88 + 28 * 82) + (horizontal * 5) - (vertical * 82 * 3) + 2
            board = board[:index] + self.player3 + board[index + 1:]
            
        if self.pos4 != 0 and self.pos4 < 100:
            if ((self.pos1 - 1)//10)%2 == 0:
                horizontal = (self.pos4 - 1) % 10
                vertical = (self.pos4 - 1) // 10
            else:
                horizontal = 9 - ((self.pos4 - 1) % 10)
                vertical = (self.pos4 - 1) // 10
            index = (88 + 28 * 82) + (horizontal * 5) - (vertical * 82 * 3) + 3
            board = board[:index] + self.player4 + board[index + 1:]

        # return the board
        
        return board
        
            

