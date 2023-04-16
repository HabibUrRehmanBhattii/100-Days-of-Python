print('Welcome to Roller Coaster!\n')
height = int(input('What is you height enter in centimeter\n'))
bill = 0

if height >= 120:
    print('You can ride!\n')
    age = int(input(print('What is your age?\n')))
    if age < 12:
        bill = 5
        print(f'Child tickets are ${bill}')
    elif age <= 18:
        bill = 7
        print(f'Youth tickets are ${bill} ')
    elif 45 <= age <= 55:
        print('Everything is going to be ok. Have a free ride on us!')
    else:
        bill = 12
        print(f'Adult tickets are ${bill}')

    wants_phot = input('Do you want a photo taken? Y or N.').lower()
    if wants_phot == 'y':
        bill += 3
        print(f'You final bill is ${bill}')
else:
    print('You cannot ride! Sorry you have to Grow up!\n')





