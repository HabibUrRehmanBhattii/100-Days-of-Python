# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         number =  "FizzBuzz"
#     elif number % 5 == 0:
#         number = "Buzz"
#     elif number % 3 == 0:
#         number = "Fizz"
#     print(number, end="\n")


# Or 

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)

# # Or

# for number in range(1, 101):
#     output = ""
#     if number % 3 == 0:
#         output += "Fizz"
#     if number % 5 == 0:
#         output += "Buzz"
#     if output == "":
#         output = number
#     print(output)


# Or

for number in range(1, 101):
    output = ""
    if number % 3 == 0:
        output += "Fizz"
    if number % 5 == 0:
        output += "Buzz"
    print(output or number)

