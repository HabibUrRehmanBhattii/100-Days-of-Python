import tkinter as tk


print('Welcome to Python Pizza Deliveries!\n')
size = str(input('What size pizza do you want? S, M, or L\n').lower())
pepperoni = str(input('Do you want pepperoni? Y or N\n').lower())
extra_cheese = str(input('Do you want extra cheese? Y or N\n').lower())

bill = 0

if size == 'S':
    bill += 15
elif size == 'm':
    bill += 20
else:
    bill += 25

if pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'y':
    bill += 1

# if size == 's':
#     bill += 15
#     if pepperoni == 'y':
#         bill += 2
#     if extra_cheese == 'y':
#         bill += 1
# if size == 'm':
#     bill += 20
#     if pepperoni == 'y':
#         bill += 3
#     if extra_cheese == 'y':
#         bill += 1
# if size == 'l':
#     bill += 25
#     if pepperoni == 'y':
#         bill += 3
#     if extra_cheese == 'y':
#         bill += 1

print(f'Your Final bill will be ${bill}')
