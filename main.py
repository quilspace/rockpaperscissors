import random

while True: 
    print("Pick option between \n R for Rock, \n P for paper, \n S for Scissors: ")
    player_action = input("input: ").upper()
    while player_action != 'R' and player_action != 'P' and player_action != 'S':
        player_action = input('Error! Not among our options. \n Enter valid input: ').upper()

    if player_action == 'R':
        player_choice = 'Rock'
    elif player_action == 'P':
        player_choice = 'paper'
    else:
        player_choice = 'scissor'
    
    possible_options = ["R", "P", "S"]
    cpu_action = random.choice(possible_options)
    if cpu_action == 'R':
        cpu_choice = 'Rock'
    elif cpu_action == 'P':
        cpu_choice = 'Paper'
    else:
        cpu_choice = 'Scissors'
    print(f"\nPlayer ( {player_choice} ) : CPU ( {cpu_choice} )\n")    


    while player_action == cpu_action:
        player_action = input("it's a tie. Play again ... \n input: ")
       
    if player_action == "R":
        if cpu_action == "S":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
    elif player_action == "P":
        if cpu_action == "R":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
    elif player_action == "S":
        if cpu_action == "P":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    