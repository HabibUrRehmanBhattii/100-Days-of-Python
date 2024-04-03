names =["Angela", "Ben", "Jenny", "Michael", "Chloe"]


# names_string contains the input values provided.
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random as r


max_names =len(names)

print(max_names)

random_number = r.randint(0, max_names - 1)

print(names[random_number] + " is going to pay the bills")





