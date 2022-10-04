# 3.3 Leap Year Exercise
# Instructions
# Write a program that works out whether if a given year is a leap year.

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
           
# This is a nested if statement. The code checks if the year is divisible by 4. If it is, it checks if the year is divisible by 100. If it is, it checks if the year is divisible by 400. If it is, it prints "Leap year.". If it is not, it prints "Not leap year.". If it is not, it prints "Leap year.". If it is not, it prints "Not leap year.".


