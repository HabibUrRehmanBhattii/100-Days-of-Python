# Functions for the 10 day challenge

# challenge 1

# def challenge1():
#     print("Challenge 1: Fizz Buzz")
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
#     print()
    
# Title Case 

# def challenge2():
#     print("Challenge 2: Print a string in Title Case")
#     print("Enter a string to convert to Title Case")
#     title = input()
#     print(title.title())
#     print()
    

# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
    
# format_name("habib", "HABIB")


# Return a string in Title Case

from turtle import title


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide vaild inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))


# def challenge3():
#     print("Challenge 3: Days in Month")
#     print("Enter a month number")
#     month = int(input())
#     months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month > 12 or month < 1:
#         print("Invalid month")
#     else:
#         days_in_month = months[month - 1]
#         print(days_in_month)
#     print()
    
# challenge3()

# # challenge 4 Leap Year Calculator

# def challenge4():
#     print("Challenge 4: Calculate Leap Year")
#     print("Enter a year")
#     year = int(input())
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("Leap year.")
#             else:
#                 print("Not leap year.")
#         else:
#             print("Leap year.")
#     else:
#         print("Not leap year.")
    
# challenge4()


# # Challenge 5 - Gererate a random number

# def challenge5():
#     print("Challenge 5: Generate a random number")
#     print("Enter a number between 1 and 100")
#     num = int(input())
#     import random
#     random_num = random.randint(1, 100)
#     if num == random_num:
#         print("You got it!")
#     else:
#         print("Sorry, it's wrong.")
#     print()
    
# challenge5()

# # challenge 8 Guess a number

# def challenge6():
#     print("Challenge 6: Guess a number")
#     print("Enter a number between 1 and 10")
#     num = int(input())
#     import random
#     random_num = random.randint(1, 10)
#     if num == random_num:
#         print("You got it!")
#     else:
#         print("Sorry, it's wrong.")
#     print()
    
# challenge6()

# # challenge 7 Print a pattern

# def challenge7():
#     print("Challenge 7: Print a pattern")
#     print("Enter a number between 1 and 10")
#     num = int(input())
#     for i in range(1, num + 1):
#         print("*" * i)
#     print()
    
# challenge7()


