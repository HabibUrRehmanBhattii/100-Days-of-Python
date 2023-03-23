# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bill = 0

#  Here if and elif statements are used to calculate the bill

# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2
#         if extra_cheese == "Y":
#             bill += 1
# elif size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
#         if extra_cheese == "Y":
#             bill += 1
# elif size == "L":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
#         if extra_cheese == "Y":
#             bill += 1
# else:
#     print("Please choose a size")


# print(f"Your final bill is: ${bill}")


# Here you can see that I have used the elif statement to make the code more efficient. I have also used the +=
# operator to make the code more efficient.

# I have also used the else statement to make sure that the user chooses a size.

# I have also used the f string to make the code more efficient.


#  Alternative solution

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        var = bill + 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your bill is: ${bill}")

#  Here I have used the elif statement to make the code more efficient. I have also used the +=
# operator to make the code more efficient.

# I have also used the else statement to make sure that the user chooses a size.
