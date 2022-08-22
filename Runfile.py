import SL
import Dice
import STB

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

    players = 0
    while players == 0:
        
        try:
            players = int(input('How many physical players are playing: '))
            
            if players <=4 and players >= 1:
                physical = players
            else:
                print('please input a number from 1 to 4')
                players = 0

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
            if status == 'cont':
                print('player ' + str(turn) + '(' + tokens[turn-1] + ')' + "'s turn")
            if physical - turn >= 0 and status == 'cont':
                input('Enter any key to roll the dice: ')
                dice = Dice.Dice()
                add = dice.diceNum()
                print(str(dice))
                status = sgame.playeradd(turn,add)
                print(sgame.printBoard())
            elif status == 'cont':
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
        input('Enter any key to roll the dice: ')
        dice = Dice.Dice()
        dice2 = Dice.Dice()
        add = dice.diceNum() + dice2.diceNum()
        print(str(dice) + str(dice2))
        status = stb.diceRoll(add)
        if status == 'cont':
            picks = 0
            while picks == 0:
                try:
                    picks = int(input('Input 1 or 2 numbers you would like to use without any space (eg: 1 | 23 | 46): '))
                    if picks <= 0 or len(str(picks)) > 2:
                        print('please enter a valid number')
                        picks = 0
                    else:
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
        print(status)
            
######################################
#
# ludo
#
######################################












