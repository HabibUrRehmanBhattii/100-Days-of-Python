print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $\n"))
split = int(input("How many people to split the bill?\n"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

total_tip = tip / 100 * bill
total_bill = bill + total_tip
per_person = round(total_bill / split, 2)

print(f"Each person should pay: ${per_person}")
