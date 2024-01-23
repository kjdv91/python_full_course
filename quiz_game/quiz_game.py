import random

choices = ["rock", "paper","scissors",]
player = None
computer = random.choice(choices)


while player not  in choices:
    player = input("rock, paper, scissors?: \n")

    print(f'Computer:  {computer}')
    print(f'Player:  {player}')

    if player == computer:
        print(f'Computer:  {computer}')
        print(f'Player:  {player}')
        print('Tie!')

    elif player == "rock":
        if computer == "paper":
            print(f'Computer:  {computer}')
            print(f'Player:  {player}')
            print('You lose!')

        if computer == "scissors":
            print(f'Computer:  {computer}')
            print(f'Player:  {player}')
            print('You win!')

    elif player == "scissors":
        if computer == "rock":
            print(f'Computer:  {computer}')
            print(f'Player:  {player}')
            print('You lose!')

        if computer == "papers":
            print(f'Computer:  {computer}')
            print(f'Player:  {player}')
            print('You win!')

    elif player == "paper":
        if computer == "scissors":
            print(f'Computer:  {computer}')
            print(f'Player:  {player}')
            print('You lose!')

        if computer == "rock":
            print(f'Computer:  {computer}')
            print(f'Player:  {player}')
            print('You win!')

    player_again = input("Play again? (yes/no):").lower()

    if player_again != "yes":
        break
print("Bye!")