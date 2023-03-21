# 31. Nested if statements and elif statements

print("Welcome to the roller-coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the roller-coaster!\n")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}.\n")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are  ${bill}.\n")
    else:
        bill = 12
        print(f"Adult tickets are pay ${bill}.\n")

    photo_taken = input('Do you want a phot taken? Y or N.').lower()

    if photo_taken == 'y':
        bill += 3
        print(f'Your total bill bit ${bill}')
else:
    print("Sorry, you have to grow taller before you can ride.")


#  In the code above, we have nested if statements. We have an if statement inside another if statement. The code checks if the height is greater than 120. If it is, it prints "You can ride the rollercoaster!". If it is not, it prints "Sorry, you have to grow taller before you can ride.".

#  We have also used elif statements. The code checks if the height is greater than 120. If it is, it prints "You can ride the rollercoaster!". If it is not, it checks if the height is greater than 110, if it is, it prints "You can ride the rollercoaster when you are with a parent". If it is not, it checks if the height is greater than 100, if it is, it prints "You can ride the rollercoaster when you are with a parent and a sibling". If it is not, it prints "Sorry, you have to grow taller before you can ride.".

