age = input('What is your current age?')

# For one year
max_month_in_year = 12
max_week_in_year = 52
max_days_in_year = 365

# For 90 year
max_age_in_days = max_days_in_year * 90
max_age_in_month = max_month_in_year * 90
max_age_in_weeks = max_week_in_year * 90

x = max_age_in_days - (int(age) * max_days_in_year)
y = max_age_in_weeks - (int(age) * max_week_in_year)
z = max_age_in_month - (int(age) * max_month_in_year)

print(f'You have {x} days, {y} weeks and {z} month lefts till 90 year old')