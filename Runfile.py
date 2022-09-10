import SL
import Dice
import STB
import Ludo
import YD

# choosing the game

print('''
_______________________________________
_______________________________________

            Choose a game
_______________________________________
_______________________________________

(1): Snake and Ladders
(2): Shut the Box
(3): Ludo
(4): Yatzee Dice
''')

choice = 0
while choice == 0:
    
    try:
        gameChoice = int(input('Choose a game to play: '))
        
        if gameChoice <=4 and gameChoice >= 1:
            choice = gameChoice
        else:
            print('please input one of the number displayed')

    except:
        print('please input a number')


######################################
#
# snake and ladders
#
######################################



if gameChoice == 1:
    print('''
_______________________________________
_______________________________________

          Snake and Ladders
_______________________________________
_______________________________________


this game is a 4 player game
''')
    # deciding how many physical players
    players = 0
    while players == 0:
        try:
            players = int(input('How many physical players are playing: '))
            
            try:
                assert players <= 4 and players >= 1
            except:
                print('please input a number from 1 to 4')
                players = 0
            else:
                physical = players

        except:
            print('please input a number')

    status = 'cont'
    sgame = SL.SL()
    phys = 0
    tokens = ['\u2660', '\u2663', '\u2665', '\u2666']
    for i in range(physical):
        phys += 1
        print('physical player ' + str(phys) + ' = ' + tokens[phys - 1])
    phys = 0
    for i in range(4 - physical):
        phys += 1
        print('computer player ' + str(phys) + ' = ' + tokens[phys - 1])
    plturn = 1    
    while status == 'cont':
        wonstate = 0
        for i in range(4):
            turn = plturn % 4
            if turn == 0:
                turn = 4
            if status == 'cont': # showing the player up next
                print('player ' + str(turn) + '(' + tokens[turn-1] + ')' + "'s turn")
            if physical - turn >= 0 and status == 'cont': # physical player input
                input('Enter any key to roll the dice: ')
                dice = Dice.Dice()
                add = dice.diceNum()
                print(str(dice))
                status = sgame.playeradd(turn,add)
                print(sgame.printBoard())
            elif status == 'cont': # computer player input
                dice = Dice.Dice()
                add = dice.diceNum()
                print(str(dice))
                status = sgame.playeradd(turn,add)
                print(sgame.printBoard())
            if status != 'cont' and wonstate == 0:
                print('player ' + status[3] + ' won!')
                wonstate = 1
            plturn += 1
    
######################################
#
# shut the box
#
######################################




if gameChoice == 2:
    print('''
_______________________________________
_______________________________________

            Shut the box
_______________________________________
_______________________________________


this game is a 1 player game
''')

    stb = STB.STB()
    status = 'cont'
    while status == 'cont':
        print(stb.printGame())
        input('Enter any key to roll the dice: ') # player input
        dice = Dice.Dice()
        dice2 = Dice.Dice()
        add = dice.diceNum() + dice2.diceNum()
        print(str(dice) + str(dice2))
        status = stb.diceRoll(add)
        if status == 'cont': # while not game over
            picks = 0
            while picks == 0:
                try:
                    picks = int(input('Input 1 or 2 numbers you would like to use without any space (eg: 1 | 23 | 46): '))
                    if picks <= 0 or len(str(picks)) > 2:
                        print('please enter a valid number')
                        picks = 0
                    else: # error handling
                        if len(str(picks)) == 2:
                            pick = stb.pickNum(int(str(picks)[0]), int(str(picks)[1]))
                        else:
                            pick = stb.pickNum(picks)
                        if pick == 'n1err':
                            print('your first number is invalid')
                            picks = 0
                        elif pick == 'n2err':
                            print('your second number is invalid')
                            picks = 0
                        elif pick == 'adderr':
                            print('your number(s) do/does not add up to the dice roll')
                            picks = 0
                except:
                    print('please input a number')
        print(status) # prints game over or win
            
######################################
#
# ludo
#
######################################


if gameChoice == 3:
    print('''
_______________________________________
_______________________________________

                 Ludo
_______________________________________
_______________________________________


this game is a 4 player game
''')
    # deciding how many physical players
    players = 0
    while players == 0:
        try:
            players = int(input('How many physical players are playing: '))
            
            try:
                assert players <= 4 and players >= 1
            except:
                print('please input a number from 1 to 4')
                players = 0
            else:
                physical = players

        except:
            print('please input a number')

    status = 'cont'
    sgame = Ludo.Ludo()
    phys = 0
    tokens = ['\u2660', '\u2663', '\u2665', '\u2666']
    for i in range(physical):
        phys += 1
        print('physical player ' + str(phys) + ' = ' + tokens[phys - 1])
    phys = 0
    for i in range(4 - physical):
        phys += 1
        print('computer player ' + str(phys) + ' = ' + tokens[phys - 1])
    plturn = 1
    while status == 'cont' or status == 'houseerr' or status == 'completeerr':
        wonstate = 0
        for i in range(4):
            turn = plturn % 4
            if turn == 0:
                turn = 4
            if status == 'cont' or status == 'houseerr' or status == 'completeerr':
                print('player ' + str(turn) + '(' + tokens[turn-1] + ')' + "'s turn")
            if physical - turn >= 0 and (status == 'cont' or status == 'houseerr' or status == 'completeerr'): # physical player input
                input('Enter any key to roll the dice: ')
                dice = Dice.Dice()
                add = dice.diceNum()
                print(str(dice))

                peicet = 0
                while peicet == 0:
                    try:
                        peicet = int(input('Which peice are you moving (1 for furtherst ahead and 4 for furthest behind: '))
                
                        if peicet <=4 and peicet >= 1:
                            peice = peicet

                            status = sgame.playeradd(turn, 4 - peice, add)
                            if status == 'houseerr':
                                print('a peice not on the board can only enter the board if you roll a 6')
                            elif status == 'completeerr':
                                print('this peice has already reached the end of the map')
                                peicet = 0
                                
                        else:
                            print('please input a number from 1 to 4')
                            peicet = 0

                            
                    except:
                        print('please input a number')
                        
                print(sgame.printBoard())
            elif status == 'cont' or status == 'houseerr' or status == 'completeerr':
                dice = Dice.Dice()
                add = dice.diceNum()
                print(str(dice))

                # computer player decision making and input

                check = 0
                if add == 6:
                    if turn == 1:
                        if 0 in sgame.pos1:
                            status = sgame.playeradd(turn, 0, add)
                            check = 1
                    elif turn == 2:
                        if 0 in sgame.pos2:
                            status = sgame.playeradd(turn, 0, add)
                            check = 1
                    elif turn == 3:
                        if 0 in sgame.pos3:
                            status = sgame.playeradd(turn, 0, add)
                            check = 1
                    else:
                        if 0 in sgame.pos4:
                            status = sgame.playeradd(turn, 0, add)
                            check = 1

                if turn == 1:
                    for i, e in enumerate(sgame.pos1):
                        if e < 57 and check == 0:
                            status = sgame.playeradd(turn, i, add)
                            check = 1
                elif turn == 2:
                    for i, e in enumerate(sgame.pos2):
                        if e < 57 and check == 0:
                            status = sgame.playeradd(turn, i, add)
                            check = 1
                elif turn == 3:
                    for i, e in enumerate(sgame.pos3):
                        if e < 57 and check == 0:
                            status = sgame.playeradd(turn, i, add)
                            check = 1
                else:
                    for i, e in enumerate(sgame.pos4):
                        if e < 57 and check == 0:
                            status = sgame.playeradd(turn, i, add)
                            check = 1
                    
                        
                print(sgame.printBoard())
            if (status != 'cont' and status != 'houseerr' and status != 'completeerr') and wonstate == 0: # printing a winner
                print('player ' + status[3] + ' won!')
                wonstate = 1
            plturn += 1

######################################
#
# yahtzee dice
#
######################################

if gameChoice == 4:
    print('''
_______________________________________
_______________________________________

            Yahtzee Dice
_______________________________________
_______________________________________


this game is a 2 physical player game
''')

    players = 0
    player = 0

    YD = YD.YD()
    print(YD.printBoard())

    for i in range(26):
        player = (player + 1)%2
        if player == 0:
            player = 2
        
        print("It's player " + str(player) + "'s turn.") # showing the player up next
        input('Enter any key to roll the 5 dice: ') # 1st roll
        dice = Dice.Dice()
        dice2 = Dice.Dice()
        dice3 = Dice.Dice()
        dice4 = Dice.Dice()
        dice5 = Dice.Dice()
        print(str(dice) + str(dice2) + str(dice3) + str(dice4) + str(dice5))

        
        keep = [dice.diceNum(), dice2.diceNum(), dice3.diceNum(), dice4.diceNum(), dice5.diceNum()]

        players = 0
        while players == 0:
            try:
                dicek = int(input('Which dice do you want to keep (eg: 125, keep the 1st, 2nd and 5th dice): '))
            
                try:
                    for i in str(dicek):
                        assert int(i) <= 5 and int(i) >= 1
                except:
                    print('please input a numbers from 1 to 5') 
                    players = 0
                else:
                    players = 1
    
            except:
                print('please input a number')

        chosen = ''
        for i in ['1','2','3','4','5']:
            if i in str(dicek):
                chosen += i
        
        keep1 = []
        for i in str(chosen):
            keep1.append(keep[int(i) - 1])
        keep = keep1

        still = 5 - len(str(chosen))
        left = []

        if still > 0:
            for i in range(still): # 2nd roll
                dice6 = Dice.Dice()
                print(str(dice6))
                left.append(dice6.diceNum())

            players = 0
            while players == 0:
                try:
                    dicek = int(input('Which dice do you want to keep (eg: 125, keep the 1st, 2nd and 5th dice): '))
                
                    try:
                        for i in str(dicek):
                            assert int(i) <= 5 and int(i) >= 1
                    except:
                        print('please input a numbers from 1 to 5')
                        players = 0
                    else:
                        players = 1
        
                except:
                    print('please input a number')

            chosen = ''
            for i in ['1','2','3','4','5']:
                if i in str(dicek):
                    chosen += i
            
            for i in str(chosen):
                keep.append(left[int(i) - 1])

            still = 5 - len(keep)
            left = []

            if still > 0:
                for i in range(still): # 3rd roll
                    dice6 = Dice.Dice()
                    keep.append(dice6.diceNum())

        print(keep) # the final 5 dice
        print(YD.printBoard()) # allowing the player to see their options

        players = 0
        while players == 0:
                try:
                    box = int(input('Which box would you like to check (eg: 12, enter score for yahtzee): '))
                
                    try:
                        assert box >= 1 and box <= 13

                    except:
                        print('please input a number from 1 to 13')
                        
                    else:
                        players = 1
                        check = YD.enter(keep, box, player)
                        if check == 'usederr':
                            print('that box has already been checked')
                            players = 0
        
                except:
                    print('please input a number')
                    
        print(YD.printBoard())


    score = YD.total() # winner after filling in all the boxes
    if score[0] + score[2] > score[1] + score[3]:
        print('Player 1 wins!')
    elif score[1] + score[3] > score[0] + score[2]:
        print('Player 2 wins!')
    else:
        print('Draw!')
        
            
        


    


