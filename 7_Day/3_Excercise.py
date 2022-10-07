#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# while "_" in display:
#     guess = input("Guess a letter: ").lower()

# #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#             print(display)
    
#     if "_" not in display:
#         print("You Win")

# OR

while "_" in display:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
print("You Win")



# This in words is:
# 1. Create a while loop that will run as long as there are still blanks in the display.
# 2. Inside the while loop, ask the user for a guess.
# 3. Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# 4. If the user guessed a letter that is in the chosen_word, then reveal that letter in the display at each position it occurs.
# 5. Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# 6. If the letter is not in chosen_word, print out the letter and let them know it's not in the word.