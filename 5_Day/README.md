# 5 Day

# 50. Using the for loop with Python Lists

For loops in python are used to iterate over a sequence of objects. In this case, we will be using a list of numbers. The for loop will iterate over the list and print each number in the list.

 The syntax for a for loop is: for item in list: print(item) 

```python
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]
 for number in numbers: print(number)
```

# 51.  [Interactive Coding Exercise] Average Height

You are going to write a program that calculates the average student height from a List of heights. 
## Average Height
# Instructions

You are going to write a program that calculates the average student height from a List of heights. 

e.g. `student_heights = [180, 124, 165, 173, 189, 169, 146]`

The average height can be calculated by adding all the heights together and dividing by the total number of heights. 

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = **1146**

There are a total of **7** heights in `student_heights`

1146 ÷ 7 = **163.71428571428572**

Average height rounded to the nearest whole number = **164**

**Important** You should not use the `sum()` or `len()` functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Example Input 

```
156 178 165 171 187
```

In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

# Example Output 

```
171
```

e.g. When you hit **run**, this is what should happen: 

 
![](https://cdn.fs.teachablecdn.com/Nzb8hUVsQJ6STAGnvDCP)
 

# Hint

1. Remember to use the `round()` function to round the average height before you print it.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[Starter Code](https://repl.it/@appbrewery/day-5-1-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 

# Solution

[Solution](https://repl.it/@appbrewery/day-5-1-solution)

# 52. [Interactive Coding Exercise] High Score

You are going to write a program that calculates the highest score from a List of scores.

## Highest Score
# Instructions

You are going to write a program that calculates the highest score from a List of scores. 

e.g. `student_scores = [78, 65, 89, 86, 55, 91, 64, 89]`

**Important** you are not allowed to use the max or min functions. The output words must match the example. i.e 

> `The highest score in the class is: x`

# Example Input 

```
78 65 89 86 55 91 64 89
```

In this case, student_scores would be a list that looks like: `[78, 65, 89, 86, 55, 91, 64, 89]`

# Example Output 

```
The highest score in the class is: 91
```

e.g. When you hit **run**, this is what should happen: 

  
![](https://cdn.fs.teachablecdn.com/DnSPgYNSTgeHRJ3MinHg)
 

# Hint

1. Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[Day-5-2-test-your-code](https://repl.it/@appbrewery/day-5-2-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 


# Solution

[Solution](https://repl.it/@appbrewery/day-5-2-solution)


# 53. for loops and the range() function 

The range() function allows you to generate a sequence of numbers, starting at 0 by default, and increments by 1 (by default), and ends at a specified number.

The range() function is useful when you want to loop through a set of code a specific number of times.

The syntax for the range() function is: range(start, stop, step)

The start parameter is optional. If omitted, the range starts at 0.

The step parameter is also optional. If omitted, the value of step is 1.

The stop parameter is required. This specifies the number at which the sequence of numbers stops.

```python
# Example of range() function
for number in range(1, 10, 3): print(number)
``` 

# 54. [Interactive Coding Exercise] Adding Even Numbers

## Adding Evens
# Instructions

You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

# Hint

1. There are quite a few ways of solving this problem, but you will need to use the `range()` function in any of the solutions.

# Solution

[solution](https://repl.it/@appbrewery/day-5-3-solution)


# 55. [Interactive Coding Exercise] The FizzBuzz Job Interview Question

## FizzBuzz
# Instructions

You are going to write a program that automatically prints the solution to the FizzBuzz game. 

> `Your program should print each number from 1 to 100 in turn.` 

>   `When the number is divisible by 3 then instead of printing the number it should print "Fizz".` 

>     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 

>       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

e.g. it might start off like this:

```
`1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz`
```

`.... etc.`

# Hint

1. Remember your answer should start from 1 and go up to and including 100. 

2. Each number/text should be printed on a separate line.

# Solution

[https://repl.it/@appbrewery/day-5-4-solution](https://repl.it/@appbrewery/day-5-4-solution)

Alternatively: [https://en.wikipedia.org/wiki/Fizz_buzz](https://en.wikipedia.org/wiki/Fizz_buzz)


# 56. Day 5 Project: Create a Password Generator

## Password Generator Project
# Instructions

You are going to write a **Password Generator** program which generates a random password for the user.

e.g. `4 letter word + 4 digit number = JduE&!91`

e.g. `6 letter word + 2 digit number = g^2jk8&P`

**Important**: The order of the letters and numbers in the password should be random.

**Hint**: You can use the `random.choice()` function to randomly select a character from a list of characters.

e.g.

```python
import random

random_char = random.choice(["a", "b", "c", "d", "e"])
print(random_char)
```


# Example Output

```
4 letter word + 4 digit number = JduE&!91
6 letter word + 2 digit number = g^2jk8&P
```

e.g. when you hit **run**, this is what should happen:


![](https://cdn.fs.teachablecdn.com/5ZQ9QZQ8QX6Q2Q2Q2Q2Q)


2. There are many ways of solving this problem, but you will need to use the random.choice() function, which you can read about [here](https://docs.python.org/3/library/random.html#random.choice).

3. You may also want to look at the [join()](https://www.w3schools.com/python/ref_string_join.asp) function which allows you to join together strings in a list together with a string separator. For example:

```python
letters = ["a", "b", "c"]
print("".join(letters))
```

# Solution

[https://repl.it/@appbrewery/day-5-5-solution](https://repl.it/@appbrewery/day-5-5-solution)




