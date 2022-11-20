
print('Welcome to the tip calculator.')

totalBill = int(input('What was the total bill?\n'))

split = int(input('How many people to split the bill?\n'))

percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? \n'))


result = totalBill / split * percentage


print('Each person should pay: $' + result)




