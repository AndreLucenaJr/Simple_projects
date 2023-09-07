import random

Play_again = True

#Create the menu of the game
def menu():
    while Play_again:
        print('[1] for even \n[2] for odd')
        player1_choose = int(input('Make your play: '))
        
        player1_number = int(input('Choose a number from 1 to 9: '))
        player2_number = random.randint(1,9)
        
        if player1_choose == 1 or player1_choose == 2:
        
            sum = player1_number + player2_number

        win_lose(player1_choose,sum)

        play_again()
       
        
    
#Win and lose condition
def win_lose(player1_choose, sum):
    if player1_choose == 1 and (sum % 2) == 0 or player1_choose == 2 and (sum % 2) == 1:
        print(f'Player 1 win, because choose even and the number was {sum}') 
    else:
        print(f'Player 2 win, because choose even and the number was {sum}') 



def play_again():
    global Play_again
    again = int(input('[1]y [2]n Play again? '))
    if again == 1:
        Play_again = True
    else:
        Play_again = False
        
    return Play_again
    

menu()
