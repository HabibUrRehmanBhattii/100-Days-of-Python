# 🚨 Don't change the code below 👇
import string

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


firstName = name1.lower()
secondName = name2.lower()

T = firstName.count("t") + secondName.count("t")
R = firstName.count("r") + secondName.count("r")
U = firstName.count("u") + secondName.count("u")
E = firstName.count("e") + secondName.count("e")

trueTotal = T + R + U + E

L = firstName.count("l") + secondName.count("l")
O = firstName.count("o") + secondName.count("o")
V = firstName.count("v") + secondName.count("v")
E = firstName.count("e") + secondName.count("e")

loveTotal = L + O + V + E

loveScore = str(trueTotal) + str(loveTotal)

loveScore = int(loveScore)

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")
