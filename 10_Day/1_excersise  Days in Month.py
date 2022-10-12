def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if (month > 12 or month < 1):
      return "Invalid month"
  elif (month == 2 and is_leap(year)):
      return 29
  else:
      return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


""" The code above does the following, explained in English:
1. The function is_leap checks if the year is a leap year.
2. If it is, it returns True, if not, it returns False.
3. The function days_in_month checks if the month is a valid month (1-12)
4. If it is, it checks if it's February and if the year is a leap year.
5. If it is, it returns 29, if not, it uses the month_days list to return the number of days in the month.
6. If the month is invalid, it returns "Invalid month"
7. The code asks the user for a year and a month and then prints the result of the function days_in_month """









