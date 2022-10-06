
# this is a range() function that give all even numbers from 1 to 100 (inclusive) and print sum  
# 1. Create a total variable and set it to 0
# 2. Create a for loop that loops through all the numbers from 1 to 100 (inclusive)
# 3. Inside the for loop, check if the number is even
# 4. If the number is even, add it to the total variable
# 5. After the for loop, print the total variable



total =0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)


# Or

total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# or 

total = 0
for number in range(1, 101, 2):
    total += number
print(total)

# or

total = 0
for number in range(1, 101):
    if number % 2 != 0:
        continue # continue is used to skip the current iteration and move on to the next iteration. In this case, it skips all the odd numbers and only adds the even numbers to the total variable.
    total += number
print(total)

