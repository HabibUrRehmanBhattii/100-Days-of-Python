# 🚨 Don't change the code below 👇
import string


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


firstName = name1.lower()
secondeName = name2.lower()

T = firstName.count("t") + secondeName.count("t")
R = firstName.count("r") + secondeName.count("r")
U = firstName.count("u") + secondeName.count("u")
E = firstName.count("e") + secondeName.count("e")

trueTotal = T + R + U + E 

L = firstName.count("l") + secondeName.count("l")
O = firstName.count("o") + secondeName.count("o")
V = firstName.count("v") + secondeName.count("v")
E = firstName.count("e") + secondeName.count("e")

loveTotal = L + O + V + E 

loveScore = str(trueTotal) + str(loveTotal)

loveScore = int(loveScore)

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")
    