import random

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

#Write your code below this line 👇

game = [rock, paper, scissors]
names = ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? Type 0 fot the Rock, 1 for Paper or 2 for Scissors"))

user_selected_image = game[user_choice]
user_selected_name = names[user_choice]

print(f"You chose {user_selected_name}:\n {user_selected_image}")

computer_choice = random.randint(0, 2)

computer_choice_names = names[computer_choice]
computer_choice_image = game[computer_choice]

print(f"Computer chose {computer_choice_names}:\n {computer_choice_image}")


if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You Win")
else:
    print("Computer Win")


