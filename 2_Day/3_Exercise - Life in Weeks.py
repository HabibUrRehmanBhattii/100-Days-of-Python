age = input("What is your current age?")

# For One Year
max_month_in_year = 12
max_week_in_year = 52
max_days_in_year = 365

# For 90 Year
max_age_in_days = 32850  
max_age_in_month = 1080
max_age_in_weeks = 4680

# IF you are one year Old

x = max_age_in_days - (int(age) * max_days_in_year)
y = max_age_in_weeks - (int(age) * max_week_in_year)
z = max_age_in_month - (int(age) * max_month_in_year)

#  Printing out the result 

print(f"You have {x} days, {y} weeks, and {z} month left")