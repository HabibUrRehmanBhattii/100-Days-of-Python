import random

word_list = ["aardvark", "baboon", "camel"]

# Todo - randomly chose a word

random_word = random.choice(word_list)

display = "_"

# Todo - ask the guest to guess a word and assigned to the blank

choice_letter = input("Please guess a word!").lower()

for letter in random_word:
    if letter == choice_letter:
        display += letter
    else:
        display = "_"
