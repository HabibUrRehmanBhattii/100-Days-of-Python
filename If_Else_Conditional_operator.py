print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# if and else statements are used to control the flow of the program and to make decisions based on conditions. Spaces are important in Python. If you don't indent the code properly, you will get an error. So, make sure you indent the code properly.


if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

# The code above is a simple example of if and else statements. The code checks if the height is greater than 120. If it is, it prints "You can ride the rollercoaster!". If it is not, it prints "Sorry, you have to grow taller before you can ride.".

# You can also use elif statements to check multiple conditions. The code below checks if the height is greater than 120, if it is, it prints "You can ride the rollercoaster!". If it is not, it checks if the height is greater than 110, if it is, it prints "You can ride the rollercoaster when you are with a parent". If it is not, it prints "Sorry, you have to grow taller before you can ride.".

height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the rollercoaster!")
elif height > 110:
    print("You can ride the rollercoaster when you are with a parent.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# You can also use multiple elif statements. The code below checks if the height is greater than 120, if it is, it prints "You can ride the rollercoaster!". If it is not, it checks if the height is greater than 110, if it is, it prints "You can ride the rollercoaster when you are with a parent". If it is not, it checks if the height is greater than 100, if it is, it prints "You can ride the rollercoaster when you are with a parent and a sibling". If it is not, it prints "Sorry, you have to grow taller before you can ride.".

height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the rollercoaster!")
elif height > 110:
    print("You can ride the rollercoaster when you are with a parent.")
elif height > 100:
    print("You can ride the rollercoaster when you are with a parent and a sibling.")
else:
    print("Sorry, you have to grow taller before you can ride.")


