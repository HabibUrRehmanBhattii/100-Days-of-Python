# Split string method
import random 


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_people = len(names)

random_selction = random.randint(0 , total_people -1)

toPay = names[random_selction]

print(f"{toPay} is going to buy the meal today!")


# or 
# pay = random.choice(names)