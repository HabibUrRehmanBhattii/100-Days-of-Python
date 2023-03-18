print('Welcome to BMI calculator\n')

weight = float(input('Enter your Weight in Kilogram\n'))
height = float(input('Enter your Height in meters\n'))

BMI: float = weight / height**2

print(f'Your BMI is {BMI}')
