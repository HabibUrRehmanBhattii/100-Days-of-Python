rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random as r

game_image = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

if player_choice >= 3 or player_choice < 0:
    print("You in put in valid value you loses")
else:
    print(game_image[player_choice])

    computer_choice = r.randint(0, 2)
    print('Computer Chosen:')
    print(game_image[computer_choice])

    if player_choice == computer_choice:
        print("It's a tie")
    elif (player_choice - computer_choice) % 3 == 1:
        print("You win")
    else:
        print("Computer wins")
