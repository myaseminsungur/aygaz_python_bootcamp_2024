import random

def game_intro():
    print("🎉 Welcome to the Rock, Paper, Scissors Arena! 🎉\n\nAre you ready? Because you're up against a tough opponent: The Computer! 💻\n\nThe rules are simple:\n🔥 The first to win two rounds becomes the champion!\n✂️ In each round, choose between 'Rock', 'Paper', or 'Scissors'.\n🔄 After each round, you'll be asked if you want to play again. If both of you say 'yes', the game continues.\n\nGame Rounds:\n🔹 Rock crushes Scissors!\n🔹 Paper wraps Rock!\n🔹 Scissors cut Paper!\n\nIf you're ready, step into the arena! 🏆 Type 'Exit' anytime to leave the game.\n\nMay the best player win! 🎮")



def rps(player,computer):
    player = player.lower()
#    print(f"Player's choice: {player}")
#    print(f"Computer's choice: {computer}")
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[player] == computer:
        return "Player won!"
    if beats[computer] == player:
        return "Computer won!"
    return "Draw!"    


# Function to display game results
def display_results(player_choice, computer_choice, result, score, round_number,game_count):
    print("\n" + "="*40)
    print(f" Game {game_count} - Round {round_number}")
    print("="*40)
    print(f" Player's choice: {player_choice.capitalize()}")
    print(f" Computer's choice: {computer_choice.capitalize()}")
    print("\n" + "-"*40)
    print(f" Result: {result}")
    print("-"*40)
    print(f" Score: Player {score['player']} - Computer {score['computer']}")
    print("="*40 + "\n")


def tas_kagit_makas_YASEMIN_SUNGUR():

    #game_intro()
    options = ['rock', 'paper', 'scissors']
    score_board = {'competitors':{'player': 0,
                  'computer': 0},
                  'round': 0}
    game_count = 1

    while True:
        
        player_choice = input("Dear Player, choose one: 'rock', 'scissors', or 'paper':\n")
        computer_choice = random.choice(options)
        
        while player_choice.lower() not in options:
            print(f"Please choose from {options}")
            player_choice = input("Dear Player, choose one: 'rock', 'scissors', or 'paper'.")
            
    
        result = rps(player_choice,computer_choice)
        if result == "Player won!":
            score_board['competitors']['player'] += 1
        elif result == "Computer won!":
            score_board['competitors']['computer'] += 1
        
        score_board['round'] += 1

        display_results(player_choice,computer_choice,result,score_board['competitors'],score_board['round'],game_count)

        if 2 in score_board['competitors'].values():
            winner = 'player' if score_board['competitors']['player'] == 2 else 'computer'
            print(f"The winner of game {game_count} - round {score_board['round']} is the {winner}.")
        else:
            continue
        
        yes_or_no = ['yes', 'no']
        yes_or_no_player = input("Do you want to play again?: Yes or No:\n")
        yes_or_no_computer = random.choice(yes_or_no)

        while yes_or_no_player.lower() not in yes_or_no:
            print(f"Please choose from {yes_or_no}")
            yes_or_no_player = input("Do you want to play again?: Yes or No:\n")
        
        if yes_or_no_computer == 'yes' and yes_or_no_player.lower() == 'yes':
            score_board = {'competitors':{'player': 0,
                          'computer': 0},
                          'round': 0}
            game_count += 1
        elif yes_or_no_computer == 'no' and yes_or_no_player.lower() == 'yes':
            print("The computer withdrew from the game! It's a coward you know :) ")
        else:
            print("It was fun! See you later :)")
            break
        

if __name__ == "__main__":
    tas_kagit_makas_YASEMIN_SUNGUR()
