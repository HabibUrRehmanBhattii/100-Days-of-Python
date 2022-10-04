# 31. Nested if statements and elif statements

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height > 120:
    print("You can ride the rollercoaster!\n")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("Please pay $5.") 
    elif age <= 18:
            print("Please pay $7")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")


#  In the code above, we have nested if statements. We have an if statement inside another if statement. The code checks if the height is greater than 120. If it is, it prints "You can ride the rollercoaster!". If it is not, it prints "Sorry, you have to grow taller before you can ride.".

#  We have also used elif statements. The code checks if the height is greater than 120. If it is, it prints "You can ride the rollercoaster!". If it is not, it checks if the height is greater than 110, if it is, it prints "You can ride the rollercoaster when you are with a parent". If it is not, it checks if the height is greater than 100, if it is, it prints "You can ride the rollercoaster when you are with a parent and a sibling". If it is not, it prints "Sorry, you have to grow taller before you can ride.".

