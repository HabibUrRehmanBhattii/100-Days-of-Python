import random
from hangman_words import word_list
from hangman_art import logo, stages

# TODO: Randomly choose a word from the word list
word_choice = random.choice(word_list).lower()
word_length = len(word_choice)
# TODO: Initialize variables for end_of_game and lives
end_of_game = False
lives = 6
# TODO: Print the logo at the start of the game
print(logo)

# TODO: Create blanks for the chosen word
#display = ["_"] * word_length
display = []
for _ in range(word_length):
    display.append("_")

while not end_of_game:
    # TODO: Ask the user to guess a letter
    guess = input("Guess the letter: ").lower()
    while len(guess) != 1 or not guess.isalpha():
        guess = input("Invalid input!  Please write only one alp abate a time").lower()
    # TODO: If the user has entered a letter they've already guessed, print the letter and let them know
    if guess in display:
        print(f"You have already guessed {guess}")
    # TODO: Check guessed letter and update the display
    for position in range(word_length):
        letter = word_choice[position]
        if letter == guess:
            display[position] = letter
    # TODO: Check if the user's guess is incorrect and update lives
    if guess not in word_choice:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was: {word_choice}")

    # TODO: Join all the elements in the list and turn it into a string
    print("".join(display))
    # TODO: Check if the user has guessed all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO: Print the stages of the hangman
    print(stages[lives])
