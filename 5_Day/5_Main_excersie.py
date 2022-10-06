#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# First need to slect two random letter form list if user say 2 then slect two random number

random_letter = ""
for letter in range(0, nr_letters):
    random_letter += random.choice(letters)

random_symbols = ""
for symbol in range(0, nr_symbols):
    random_symbols += random.choice(symbols)

random_numbers = ""
for number in range(0, nr_numbers):
    random_numbers += random.choice(numbers)


random_password = random_numbers + random_letter + random_symbols

sr = ''.join(random.sample(random_password, len(random_password)))
print(sr)

# Alternative way to do it

# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# # random the string letter
# print("".join(random.sample(password, len(password))))


# One more way to do it

# password_list = []

# for char in range(1, nr_letters + 1):
#     password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#     password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password_list += random.choice(numbers)

# random.shuffle(password_list)

# password = ""
# for char in password_list:
#     password += char

# print(f"Your password is: {password}")



