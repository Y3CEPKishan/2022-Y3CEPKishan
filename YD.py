class YD:
    def __init__(self):
        self.score1 = [90,90,90,90,90,90,90,90,90,90,90,90,90]
        self.score2 = [90,90,90,90,90,90,90,90,90,90,90,90,90]

    def eligible(self, rolls):
        # calcute the scores for each checkbox based on the 5 dice rolls
        # this makes it easier to enter the values in the tabulation
        
        pos = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in rolls:
            pos[i-1] += 1
        for i,e in enumerate(pos[:6]):
            if e >= 3:
                pos[6] = (i+1) * e * 3
                if 2 in pos[:6]:
                    pos[8] = 25
            if e >= 4:
                pos[7] = (i+1) * e * 4
            if e == 5:
                pos[11] = 50

        for i in range(3):
            if pos[i] > 0 and pos[i+1] > 0 and pos[i+2] > 0 and pos[i+3] > 0:
                pos[9] = 30
        for i in range(2):
            if pos[i] > 0 and pos[i+1] > 0 and pos[i+2] > 0 and pos[i+3] > 0 and pos[i+4]:
                pos[10] = 40
        for i,e in enumerate(pos[:6]):
            pos[i] = e * (i+1)
        pos[-1] = sum(pos[:6])
        return pos

    def enter(self, rolls, pos, player):
        # this is where the runfile enters the player inputs
        # usederr means that the box has already been filled so no more changes can be made
        
        poss = self.eligible(rolls)
        if player == 1:
            if self.score1[pos-1] == 90:
                self.score1[pos-1] = poss[pos-1]
            else:
                return 'usederr'
        if player == 2:
            if self.score2[pos-1] == 90:
                self.score2[pos-1] = poss[pos-1]
            else:
                return 'usederr'

    def total(self):
        # calculating the values for the last 3 boxes
        # this is because the total scores are dependent on the scores of the existing boxes
        
        ut1 = 0
        ut2 = 0
        lt1 = 0
        lt2 = 0
        for i in self.score1[:6]:
            if i != 90:
                ut1 += i
        for i in self.score2[:6]:
            if i != 90:
                ut2 += i
        for i in self.score1[6:]:
            if i != 90:
                lt1 += i
        for i in self.score2[6:]:
            if i != 90:
                lt2 += i

        return [ut1,lt1,ut2,lt2]
        
    def printBoard(self):

        # a gamecard
        
        card = '''
 ______________ 
|        |  1  |
| aces   |  |  |
|________|__|__|
|        |  2  |
| twos   |  |  |
|________|__|__|
|        |  3  |
| threes |  |  |
|________|__|__|
|        |  4  |
| fours  |  |  |
|________|__|__|
|        |  5  |
| fives  |  |  |
|________|__|__|
|        |  6  |
| sixes  |  |  |
|________|__|__|
| 3 of a |  7  |
| kind   |  |  |
|________|__|__|
| 4 of a |  8  |
| kind   |  |  |
|________|__|__|
|  full  |  9  |
| house  |  |  |
|________|__|__|
|  small |  10 |
|straight|  |  |
|________|__|__|
|  large |  11 |
|straight|  |  |
|________|__|__|
|        |  12 |
|YAHTZEE |  |  |
|________|__|__|
|        |  13 |
| chance |  |  |
|________|__|__|
| upper  |  |  |
| total  |  |  |
|________|__|__|
| lower  |  |  |
| total  |  |  |
|________|__|__|
| GRAND  |  |  |
| TOTAL  |  |  |
|________|__|__|
'''

        # displaying each score on the gamecard for the players
        # each box needs a specific string index that can be calculated
        
        total = self.total()
        for i,e in enumerate(self.score1):
            index = 45 + i * 3 * 17
            if e != 90 and len(str(e)) == 1:
                card = card[:index] + str(e) + card[index + 1:]
            elif e != 90 and len(str(e)) == 2:
                card = card[:index] + str(e) + card[index + 2:]
                
            if len(str(total[0])) == 1:
                card = card[:45 + 13 * 3 * 17] + str(total[0]) + card[46 + 13 * 3 * 17:]
            elif len(str(total[0])) == 2:
                card = card[:45 + 13 * 3 * 17] + str(total[0]) + card[47 + 13 * 3 * 17:]
                
            if len(str(total[1])) == 1:
                card = card[:45 + 14 * 3 * 17] + str(total[1]) + card[46 + 14 * 3 * 17:]
            elif len(str(total[1])) == 2:
                card = card[:45 + 14 * 3 * 17] + str(total[1]) + card[47 + 14 * 3 * 17:]

            if len(str(total[1] + total[0])) == 1:
                card = card[:45 + 15 * 3 * 17] + str(total[1] + total[0]) + card[46 + 15 * 3 * 17:]
            elif len(str(total[1] + total[0])) == 2:
                card = card[:45 + 15 * 3 * 17] + str(total[1] + total[0]) + card[47 + 15 * 3 * 17:]

        total = total[2:]
        
        for i,e in enumerate(self.score2):
            index = 48 + i * 3 * 17
            if e != 90 and len(str(e)) == 1:
                card = card[:index] + str(e) + card[index + 1:]
            elif e != 90 and len(str(e)) == 2:
                card = card[:index] + str(e) + card[index + 2:]

            if len(str(total[0])) == 1:
                card = card[:48 + 13 * 3 * 17] + str(total[0]) + card[49 + 13 * 3 * 17:]
            elif len(str(total[0])) == 2:
                card = card[:48 + 13 * 3 * 17] + str(total[0]) + card[50 + 13 * 3 * 17:]
                
            if len(str(total[1])) == 1:
                card = card[:48 + 14 * 3 * 17] + str(total[1]) + card[49 + 14 * 3 * 17:]
            elif len(str(total[1])) == 2:
                card = card[:48 + 14 * 3 * 17] + str(total[1]) + card[50 + 14 * 3 * 17:]

            if len(str(total[1] + total[0])) == 1:
                card = card[:48 + 15 * 3 * 17] + str(total[1] + total[0]) + card[49 + 15 * 3 * 17:]
            elif len(str(total[1] + total[0])) == 2:
                card = card[:48 + 15 * 3 * 17] + str(total[1] + total[0]) + card[50 + 15 * 3 * 17:]
                
        # returning the gamecard
        
        return card



