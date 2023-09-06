import random

#set variables
player1_wins = 0
player2_wins = 0

#Creation of the main menu of the game
def main_menu():
    print('Welcome to the Rock, Paper and Scissors game')
    print('[1] PLay Against Computer\n[2] PLay Against another player\n[3] Quit the game')
    game_mode = int(input('What is your game mode choose? '))
    game_rounds = int(input('How many rouds do you want to play? '))
    
    return game_mode,game_rounds

#Creation of the play menu
def play_menu():
    msg_play = '[1] Rock\n[2] Paper\n[3] Scissors: '
    game_mode, game_rounds = main_menu()
    
    
    for i in range (game_rounds):
        
        if game_mode == 1:
            jogador1 = int(input(msg_play))
            jogador2 = random.randint(1, 3) 
            win_lose(jogador1, jogador2)
            

        elif game_mode == 2:
             jogador1 = int(input(msg_play))
             jogador2 = int(input(msg_play))
             win_lose(jogador1, jogador2)
        
        elif game_mode == 3:
            print("End Game")
            run = False


#Win and lose Conditions
def win_lose(jogador1, jogador2):
    if jogador1 == 1 and jogador2 == 3 or jogador1 == 2 and jogador2 == 1 or jogador1 == 3 and jogador2 == 2:
        print(f"Player 1 wins {player1_wins} times")
    elif jogador1 == jogador2:
        print("Draw")
    else:
        print(f"Player 2 wins {player2_wins} times")




play_menu()



