print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    want_photo = input("Do you want a photo taken? Y or N. ")
    if want_photo == "Y":
        bill += 3
        print(f"The total bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

# want_photo = input("Do you want a photo taken? Y or N. ") is not part of the if statement. It is outside the if statement. So, it will be executed regardless of the condition. If the condition is true, it will execute the code inside the if statement. If the condition is false, it will execute the code outside the if statement.
