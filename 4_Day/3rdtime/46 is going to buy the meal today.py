names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# names_string contains the input values provided.
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

number_of_names =len(names)

random_index = random.randint(0, number_of_names -1)
#Select the random index to names
names_select = names[random_index]

print(f"{names_select } is going to buy the meal today!" )