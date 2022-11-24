# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


bmi = round(weight / height ** 2)

if bmi <= 18:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi <= 22:
    print(f"Your bmi is {bmi}, you have a normal weight")
elif bmi <= 28:
    print(f"Your bmi is {bmi}, you have a slightly overweight")
elif bmi <= 33:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")

# Here we have used elif statements. The code checks if the bmi is less than or equal to 18.5. If it is,
# it prints "Your bmi is {bmi}, you are underweight". If it is not, it checks if the bmi is less than or equal to 25.
# If it is, it prints "Your bmi is {bmi}, you have a normal weight". If it is not, it checks if the bmi is less than
# or equal to 30. If it is, it prints "Your bmi is {bmi}, you have a slightly overweight". If it is not, it checks if
# the bmi is less than or equal to 35. If it is, it prints "Your bmi is {bmi}, you are obese". If it is not,
# it prints "Your bmi is {bmi}, you are clinically obese.".
