import random
from hangman_words import word_list
from hangman_art import logo, stages

# Randomly choose a word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Print the logo at the start of the game
print(logo)

# Create blanks
display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose. The word was:", chosen_word)

    # Join all the elements in the list and turn it into a string
    print(" ".join(display))

    # Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the stages
    print(stages[lives])
