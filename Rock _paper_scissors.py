import random

#set variables


#Creation of the main menu of the game
def main_menu():
    print('-' * 50)
    print('Welcome to the Rock, Paper and Scissors game')
    print('[1] PLay Against Computer\n[2] PLay Against another player\n[3] Quit the game')
    print('-' * 50)
    game_mode = int(input('What is your game mode choose? '))
   
    return game_mode

#Creation of the play menu
def play_menu():
   
    msg_play = '[1] Rock\n[2] Paper\n[3] Scissors: '
    game_mode = main_menu()
    game_rounds = int(input('How many rouds do you want to play? ')) 

    player1_wins = 0
    player2_wins = 0
    #set the game rounds
    for i in range (game_rounds):
        
        if game_mode == 1:
            print('-' * 50)
            jogador1 = int(input(msg_play))
            print('-' * 50)
            jogador2 = random.randint(1, 3) 
            player1_wins, player2_wins = win_lose(jogador1, jogador2, player1_wins, player2_wins)
            

        elif game_mode == 2:
             print('-' * 50)
             jogador1 = int(input(msg_play))
             print('-' * 50)
             jogador2 = int(input(msg_play))
             player1_wins, player2_wins = win_lose(jogador1, jogador2, player1_wins, player2_wins)
        
        elif game_mode == 3:
            print("You close the game")
           


#Win and lose Conditions
def win_lose(jogador1, jogador2,player1_wins,player2_wins):
    
    if jogador1 == 1 and jogador2 == 3 or jogador1 == 2 and jogador2 == 1 or jogador1 == 3 and jogador2 == 2:
        print(f"Player 1 wins {player1_wins+1} times")
        player1_wins += 1
    
    elif jogador1 == jogador2:
        print("Draw")
    
    else:
        print(f"Player 2 wins {player2_wins+1} times")
        player2_wins += 1
    
    return player1_wins, player2_wins



play_menu()



