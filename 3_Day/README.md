# **Day 3 Python**

Conditional statements, Logical operators, and Code Blocks and Scope. This is a continuation of the previous day's work.

## **Conditional Statements**

Conditional statements are used to control the flow of your code. They allow you to check for certain conditions and execute code based on those conditions. In Python, we use the `if` statement to do this.

```python
if 5 > 2:
    print("Five is greater than two!")
```

The `if` statement is followed by a condition. If the condition is `True`, then the indented code block below it will be executed. If the condition is `False`, then the indented code block will be skipped.

### **Indentation**

In Python, indentation is very important. It is used to define code blocks. Code blocks are defined by their indentation. All statements with the same indentation, are part of the same block. For example:

```python
if 5 > 2:
    print("Five is greater than two!")
    print("Five is still greater than two!")
print("This is not part of the if block.")
```

The `print` statement after the `if` block is not indented, so it is not part of the `if` block.

### **Elif**

The `elif` keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

```python
if 5 > 2:
    print("Five is greater than two!")
elif 4 > 2:
    print("Four is greater than two!")
```

### **Else**

The `else` keyword catches anything which isn't caught by the preceding conditions.

```python
if 5 > 2:
    print("Five is greater than two!")
else:
    print("Five is not greater than two!")
```

### **Short Hand If**

If you have only one statement to execute, you can put it on the same line as the if statement.

```python
if 5 > 2: print("Five is greater than two!")
```

### **Short Hand If ... Else**

If you have only one statement to execute, one for if, and one for else, you can put it all on the same line.

```python
print("Five is greater than two!") if 5 > 2 else print("Five is not greater than two!")
```

### **And**

The `and` keyword is a logical operator, and is used to combine conditional statements.

```python
if 5 > 2 and 3 > 1:
    print("Both conditions are True")
```

### **Or**

The `or` keyword is a logical operator, and is used to combine conditional statements.

```python
if 5 > 2 or 3 > 1:
    print("At least one of the conditions is True")
```

### **Nested If**

You can have if statements inside if statements, this is called nested if statements.

```python
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
```

### **The pass Statement**

`if` statements cannot be empty, but if you for some reason have an `if` statement with no content, put in the `pass` statement to avoid getting an error.

```python
if 5 > 2:
    pass
```

## **Python Loops**

Python has two primitive loop commands:

- `while` loops
- `for` loops

### **The `while` Loop**

With the `while` loop we can execute a set of statements as long as a condition is true.

```python
i = 1
while i < 6:
    print(i)
    i += 1
```

### **The `break` Statement**

With the `break` statement we can stop the loop even if the while condition is true:

```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```


# **Exercise 3.1**    Odd or Even

# Instructions

Write a program that works out whether if a given number is an odd or even number. 

Even numbers can be divided by 2 with no remainder. 

e.g. 86 is **even** because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is **odd** because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The **modulo** is written as a percentage sign (%) in Python. It gives you the remainder after a division. 

e.g. 

6 ÷ 2 = 3 with no remainder. 

```
6 % 2 = 0
```

5 ÷ 2 = 2 x **2** + 1, remainder is 1.

```
5 % 2 = 1
```

14 ÷ 4 = 3 x **4** + 2, remainder is 2.

```
14 % 4 = 2
```

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops. 

# Example Input 1

```
43
```

# Example Output 1

```
This is an odd number.
```

# Example Input 2

```
94
```

# Example Output 2

```
This is an even number.
```

e.g. When you hit **run**, this is what should happen:   

![](https://cdn.fs.teachablecdn.com/bkF9TKJSTGksvxNzOtba)

# Hint

1. All even numbers can be divided by 2 with 0 remainder.
2. Try some using the modulo with some odd numbers e.g. 

```
3 % 2
```

```
5 % 2
```

```
7 % 2
```

Then try using the modulo with some even numbers e.g.

```
4 % 2
```

```
6 % 2
```

```
8 % 2
```

See what's in common each time.
 
# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-3-1-test-your-code](https://repl.it/@appbrewery/day-3-1-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 

# Solution

[https://repl.it/@appbrewery/day-3-1-solution](https://repl.it/@appbrewery/day-3-1-solution)

<hr>

# **31. Nested if statements and elif statements**

![](/3_Day/31.Nested_if_statements_and_elif_statements.png)
![](/3_Day/31.Nested_if_statements_and_elif_statements_2.png)

<hr >


# **Exercise 3.2** 
# BMI Calculator 2.0
## Instructions

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.

![](https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36)

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

![](https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv)

**Warning** you should **round** the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. **underweight, normal weight,  overweight, obese, clinically obese**. 

# Example Input

```
weight = 85
```

```
height = 1.75
```

# Example Output

85 ÷ (1.75 x 1.75) =  27.755102040816325

```
Your BMI is 28, you are slightly overweight.
```

e.g. When you hit **run**, this is what should happen:   

![](https://cdn.fs.teachablecdn.com/mGRynIETXuVqoDk8unci)

The testing code will check for print output that is formatted like one of the lines below:

```
"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."
```

Hint

1. Try to use the **exponent** operator in your code.
2. Remember to **round** your result to the nearest whole number. 
3. Make sure you include the words in **bold** from the interpretations. 

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-3-2-test-your-code](https://repl.it/@appbrewery/day-3-2-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 




# Solution

[https://repl.it/@appbrewery/day-3-2-solution](https://repl.it/@appbrewery/day-3-2-solution)

<hr>

# 3.3 Leap Year Exercise

![](/3_Day/leapYear.png)

###### 💪This is a Difficult Challenge 💪

# Instructions

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

[https://www.youtube.com/watch?v=xX96xng7sAE](https://www.youtube.com/watch?v=xX96xng7sAE)

This is how you work out whether if a particular year is a leap year. 

> `on every year that is evenly divisible by 4
>   **except** every year that is evenly divisible by 100
>     **unless** the year is also evenly divisible by 400`

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷  4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops. 

# Example Input 1

```
2400
```

# Example Output 1

```
Leap year.
```

# Example Input 2

```
1989
```

# Example Output 2

```
Not leap year.
```

e.g. When you hit **run**, this is what should happen:  

 ![](https://cdn.fs.teachablecdn.com/AthNqKoSm6JD4sMom2X2)

# Hint

1. Try to visualise the rules by creating a flow chart on www.draw.io
2. If you really get stuck, you can see the flow chart I created: 

https://bit.ly/36BjS2D

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-3-3-test-your-code](https://repl.it/@appbrewery/day-3-3-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 


# Solution

[https://repl.it/@appbrewery/day-3-3-solution](https://repl.it/@appbrewery/day-3-3-solution)


# 34. Multiple If Statements in Succession

![](/3_Day/34.Multiple_If_Statements_in_Succession.png)


# Exercise 3.4 



## Pizza Order

# Instructions

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program. 

Based on a user's order, work out their final bill. 

```
Small Pizza: $15
```

```
Medium Pizza: $20
```

```
Large Pizza: $25
```

```
Pepperoni for Small Pizza: +$2
```

```
Pepperoni for Medium or Large Pizza: +$3
```

```
Extra cheese for any size pizza: + $1
```

# Example Input

```
size = "L"
```

```
add_pepperoni = "Y"
```

```
extra_cheese = "N"
```

# Example Output

```
Your final bill is: $28.
```

e.g. When you hit **run**, this is what should happen:  

 
![](https://cdn.fs.teachablecdn.com/p1evEkwQxGNR4WlolIb4)
  

# Hint

1. Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-3-4-test-your-code](https://repl.it/@appbrewery/day-3-4-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 



# Solution

[https://repl.it/@appbrewery/day-3-4-solution](https://repl.it/@appbrewery/day-3-4-solution)

36. Logical Operators

![](/3_Day/36.Logical_Operators.png)

A logical operator is used to combine conditional statements:

```
and
```

```
or
```

```
not
```

and returns True if both statements are true:

```
x < 5 and  x < 10
```

or returns True if one of the statements is true:

```
x < 5 or x < 4
```

not reverses the result, returns False if the result is true:

```
not(x < 5 and x < 10)
```

# 3.5 Love Calculator

# Love Calculator


### 💪 This is a Difficult Challenge 💪

# Instructions

You are going to write a program that tests the compatibility between two people.  

To work out the love score between two people:

> Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 


For Love Scores **less than 10** or **greater than 90**, the message should be:

`"Your score is **x**, you go together like coke and mentos."` 

For Love Scores **between 40** and **50**, the message should be:

`"Your score is **y**, you are alright together."`

Otherwise, the message will just be their score. e.g.:

`"Your score is **z**."`

e.g. 

`name1 = "Angela Yu"`

`name2 = "Jack Bauer"`

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

# Example Input 1

```
name1 = "Kanye West"
```

```
name2 = "Kim Kardashian"
```

# Example Output 1

```
Your score is 42, you are alright together.
```

# Example Input 2

```
name1 = "Brad Pitt"
```

```
name2 = "Jennifer Aniston"
```

# Example Output 2

```
Your score is 73.
```

e.g. When you hit **run**, this is what should happen:  

![](https://cdn.fs.teachablecdn.com/nfSILIPSNaIOwWhPR5vr)

The testing code will check for print output that is formatted like one of the lines below:
```
"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."
```

# Hint

1. The `lower()` function changes all the letters in a string to lower case. 

[https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python](https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python)

2. The `count()` function will give you the number of times a letter occurs in a string. 

[https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string](https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string)

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-3-5-test-your-code](https://repl.it/@appbrewery/day-3-5-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 





# Solution

[https://repl.it/@appbrewery/day-3-5-solution](https://repl.it/@appbrewery/day-3-5-solution)

37. The Final Project

![](/3_Day/37.The_Final_Project.png)

## Treasure Island

# Instructions

Make your own "Choose Your Own Adventure" game. Use conditionals such as `if`, `else`, and `elif` statements to lay out the logic and the story's path in your program. 

[To write your code according to my story, you can use this flow chart from draw.io to help you.](https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload)

However, I think the fun part is writing your *own* story 😊

🧞‍♂️ 🐊 🧙‍♂️ 🧟 🧚‍♂️ 🧝‍♂️ 🥷 🤖 👽 🙀 

That said if you'd like to continue with my example, feel free to use the text snippets below...

### Text Snippets from my example

* 'You\'re at a crossroad. Where do you want to go? Type "left" or "right"'
* 'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
* "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
* "It's a room full of fire. Game Over."
* "You found the treasure! You Win!"
* "You enter a room of beasts. Game Over."
* "You chose a door that doesn't exist. Game Over."
* "You get attacked by an angry trout. Game Over."
* "You fell into a hole. Game Over."

# Escaping Characters

If you want to use multiple sets of quotes inside a single string, you might have to "escape" some of them using the backslash `\`. You can see this in my first sentence: 'You\'re at a crossroad...'. [More on escaping characters here.](https://www.w3schools.com/python/gloss_python_escape_characters.asp)

# Extensions

Have a think about how you might write your program to make a player's answers less case-sensitive. In other words, your code should work regardless of whether your user answers "left" or "Left".

[You can also add your own ASCII art](https://ascii.co.uk/art). Just remember to add three single quotes `'''` at the start and at the end of your artwork to turn it into a multi-line string. 


# Solution

[https://replit.com/@appbrewery/treasure-island-end#main.py](https://replit.com/@appbrewery/treasure-island-end)
