
# For loop With range
# range is a function that creates a sequence of numbers
# range(1, 10) # 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(1, 10, 2) # 1, 3, 5, 7, 9 # 2 is the step size (how many numbers to skip)  
# range(10, 0, -1) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 # 10 is the starting point, 0 is the ending point, -1 is the step size (how many numbers to skip)
# range(10) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 # 10 is the ending point, 0 is the starting point, 1 is the step size (how many numbers to skip)
# range(10, 0) # nothing # 10 is the starting point, 0 is the ending point, 1 is the step size (how many numbers to skip) 10, 9, 8, 7, 6, 5, 4, 3, 2, 1



# for number in range(1, 10):
#     print(number)

# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)



# Odd numbers from 1 to 100 (inclusive) and print sum
# total = 0
# for number in range(1, 101):
#     if number % 2 != 0:
#         total += number
# print(total)

# Even numbers from 1 to 100 (inclusive) and print sum
# total = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number
# print(total)

# Multiplication table from 1 to 10
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}", end="\t")
#         # end="\t" is a tab character to make the table look nice and neat  
#     print()
# # print() is used to print a new line after each row of the table is printed out 

# Divisible by 3 from 1 to 100 (inclusive) and print sum
# total = 0
# for number in range(1, 101):
#     if number % 3 == 0:
#         total += number
# print(total)



