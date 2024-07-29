# LESSON 19 DAY 5 - FIZZBUZZ

# I need counting from 1 to 100.

# Then i have to check if it is disvisble by both 3 and 5 . if yes fizzebuzz then if by 5 if not then by 3 ...for 3 fizze and for 5 is buzz


### Rember if it is deivisble by 5 then replace it by buzz
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)
