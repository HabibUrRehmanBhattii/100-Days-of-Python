print('Welcome to the Tip Calculator?\n')

bill = float(input('What was the total bill?\n'))
tip = int(input('What percentage tip would like to give? 10, 12 or 15\n'))
split = int(input('How many people to split the bill?\n'))

total_tip = tip / 100 * bill
total_bill = total_tip + bill
per_person = round(total_bill / split, 2)

print(f'Each person should pay: ${per_person}')







