class Ludo:

    def __init__(self):
        
        # symbol representing each player
        self.player1 = '\u2660'
        self.player2 = '\u2663'
        self.player3 = '\u2665'
        self.player4 = '\u2666'
        
        # starting each player at 0
        self.pos1 = [0,0,0,0]
        self.pos2 = [0,0,0,0]
        self.pos3 = [0,0,0,0]
        self.pos4 = [0,0,0,0]

    def playeradd(self,player,planum,roll):

        # this is where the runfile enters the player inputs
        # completeerr means that a player is trying to move a peice that has already finished
        # houseerr means that a player did not roll a 6 yet is trying to get his peice of the house
        if player == 1:
            self.pos1 = sorted(self.pos1)
            if self.pos1[planum] == 0:
                if roll != 6:
                    return 'houseerr'
                else:
                    self.pos1[planum] += 1
            elif self.pos1[planum] >= 57:
                return 'completeerr'
            else:
                self.pos1[planum] += roll
        if player == 2:
            self.pos2 = sorted(self.pos2)
            if self.pos2[planum] == 0:
                if roll != 6:
                    return 'houseerr'
                else:
                    self.pos2[planum] += 1
            elif self.pos2[planum] >= 57:
                return 'completeerr'
            else:
                self.pos2[planum] += roll
        if player == 3:
            self.pos3 = sorted(self.pos3)
            if self.pos3[planum] == 0:
                if roll != 6:
                    return 'houseerr'
                else:
                    self.pos3[planum] += 1
            elif self.pos3[planum] >= 57:
                return 'completeerr'
            else:
                self.pos3[planum] += roll
        if player == 4:
            self.pos4 = sorted(self.pos4)
            if self.pos4[planum] == 0:
                if roll != 6:
                    return 'houseerr'
                else:
                    self.pos4[planum] += 1
            elif self.pos4[planum] >= 57:
                return 'completeerr'
            else:
                self.pos4[planum] += roll


        # sorting to ensure that the peices are arranged based on their positions on the map

        self.pos1 = sorted(self.pos1)
        self.pos2 = sorted(self.pos2)
        self.pos3 = sorted(self.pos3)
        self.pos4 = sorted(self.pos4)

        # determining when a player has won
        
        pl1win = 0
        for i in self.pos1:
            if i >= 57:
                pl1win += 1
        pl2win = 0
        for i in self.pos2:
            if i >= 57:
                pl2win += 1
        pl3win = 0
        for i in self.pos3:
            if i >= 57:
                pl3win += 1
        pl4win = 0
        for i in self.pos4:
            if i >= 57:
                pl4win += 1
        if pl1win == 4:
            return 'win1'
        elif pl2win == 4:
            return 'win2'
        elif pl3win == 4:
            return 'win3'
        elif pl4win == 4:
            return 'win4'
        else:
            return 'cont'

    def printBoard(self):
        # a map of the ludo board and its peices
        a = '''
                                   ______________
                                  |    |    |    |
                                  |    |    |    |
                                  |____|____|____|
                                  |    |#p2 |#p2 |
                                  |    |    |    |
                                  |____|____|____|
                                  |    |#p2 |    |
                                  |    |    |    |
                                  |____|____|____|
                                  |    |#p2 |    |
                                  |    |    |    |
                                  |____|____|____|
                                  |    |#p2 |    |
                                  |    |    |    |
                                  |____|____|____|
                                  |    |#p2 |    |
                                  |    |    |    |
                                  |____|____|____|

 _____________________________     ______________     _____________________________
|    |#p1 |    |    |    |    |   |              |   |    |    |    |    |    |    |
|    |    |    |    |    |    |   |              |   |    |    |    |    |    |    |
|____|____|____|____|____|____|   |              |   |____|____|____|____|____|____|
|    |#p1 |#p1 |#p1 |#p1 |#p1 |   |              |   |#p3 |#p3 |#p3 |#p3 |#p3 |    |
|    |    |    |    |    |    |   |              |   |    |    |    |    |    |    |
|____|____|____|____|____|____|   |              |   |____|____|____|____|____|____|
|    |    |    |    |    |    |   |              |   |    |    |    |    |#p3 |    |
|    |    |    |    |    |    |   |              |   |    |    |    |    |    |    |
|____|____|____|____|____|____|   |______________|   |____|____|____|____|____|____|

                                   ______________
                                  |    |#p4 |    |
                                  |    |    |    |
                                  |____|____|____|
                                  |    |#p4 |    |
                                  |    |    |    |
                                  |____|____|____|
                                  |    |#p4 |    |
                                  |    |    |    |
                                  |____|____|____|
                                  |    |#p4 |    |
                                  |    |    |    |
                                  |____|____|____|
                                  |#p4 |#p4 |    |
                                  |    |    |    |
                                  |____|____|____|
                                  |    |    |    |
                                  |    |    |    |
                                  |____|____|____|
        '''

        # a list of positions for each player on the board as indexes of a atring
        # this makes each players path to the goal more linear so its easier for the calculations
        
        pos1 = [1145, 1150, 1155, 1160, 1165, 902, 749, 596, 443, 290, 137, 142, 147, 300, 453, 606, 759, 912, 1193, 1198, 1203, 1208, 1213, 1218, 1473, 1728, 1723, 1718, 1713, 1708, 1703, 1966, 2119, 2272, 2425, 2578, 2731, 2726, 2721, 2568, 2415, 2262, 2109, 1956, 1675, 1670, 1665, 1660, 1655, 1650, 1395, 1400, 1405, 1410, 1415, 1420]
        pos2 = [300, 453, 606, 759, 912, 1193, 1198, 1203, 1208, 1213, 1218, 1473, 1728, 1723, 1718, 1713, 1708, 1703, 1966, 2119, 2272, 2425, 2578, 2731, 2726, 2721, 2568, 2415, 2262, 2109, 1956, 1675, 1670, 1665, 1660, 1655, 1650, 1395, 1140, 1145, 1150, 1155, 1160, 1165, 902, 749, 596, 443, 290, 137, 142, 295, 448, 601, 754, 907]
        pos3 = [1723, 1718, 1713, 1708, 1703, 1966, 2119, 2272, 2425, 2578, 2731, 2726, 2721, 2568, 2415, 2262, 2109, 1956, 1675, 1670, 1665, 1660, 1655, 1650, 1395, 1140, 1145, 1150, 1155, 1160, 1165, 902, 749, 596, 443, 290, 137, 142, 147, 300, 453, 606, 759, 912, 1193, 1198, 1203, 1208, 1213, 1218, 1473, 1468, 1463, 1458, 1453, 1448]
        pos4 = [2568, 2415, 2262, 2109, 1956, 1675, 1670, 1665, 1660, 1655, 1650, 1395, 1140, 1145, 1150, 1155, 1160, 1165, 902, 749, 596, 443, 290, 137, 142, 147, 300, 453, 606, 759, 912, 1193, 1198, 1203, 1208, 1213, 1218, 1473, 1728, 1723, 1718, 1713, 1708, 1703, 1966, 2119, 2272, 2425, 2578, 2731, 2726, 2573, 2420, 2267, 2114, 1961]

        # printing each peice on the board
        
        for i in self.pos1:
            if i < 57 and i > 0:
                index = pos1[i-1]
                a = a[:index] + self.player1 + a[index + 1:]

        for i in self.pos2:
            if i < 57 and i > 0:
                index = pos2[i-1] + 1
                a = a[:index] + self.player2 + a[index + 1:]

        for i in self.pos3:
            if i < 57 and i > 0:
                index = pos3[i-1] + 2
                a = a[:index] + self.player3 + a[index + 1:]

        for i in self.pos4:
            if i < 57 and i > 0:
                index = pos4[i-1] + 3
                a = a[:index] + self.player4 + a[index + 1:]

        # printing each peice to the physical players for if the board becomes too complicated
        
        playerpos1 = "\nPlayer 1's peices: " + str(self.pos1) + '\n'
        playerpos2 = "Player 2's peices: " + str(self.pos2) + '\n'
        playerpos3 = "Player 3's peices: " + str(self.pos3) + '\n'
        playerpos4 = "Player 4's peices: " + str(self.pos4) + '\n'

        # returning the map and the text as one long string
        
        a = a + playerpos1 + playerpos2 + playerpos3 + playerpos4

        return a



















