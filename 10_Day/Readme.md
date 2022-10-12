Section 10: Day 10 Beginner - Functions with Outputs

# Functions with Outputs

## Introduction

In the last lesson, we learned about functions and how to use them. In this lesson, we will learn about functions with outputs.

## Objectives

You will be able to:

* Understand and explain what a function with an output is
* Understand and explain how to use a function with an output
* Understand and explain how to use a function with an output in a program

## Functions with Outputs

A function with an output is a function that returns a value. The value can be a number, a string, a list, a dictionary, or any other data type. The value is returned to the part of the program that called the function. The value is returned using the `return` statement.

## Using a Function with an Output

To use a function with an output, you need to assign the value returned by the function to a variable. The variable can then be used in the program.

## Example

The following example shows how to use a function with an output.

```python

def add(a, b):
    return a + b

result = add(2, 3)
print(result)

```

The output of the program is:

```python

5

```

## Summary

In this lesson, we learned about functions with outputs. We learned that a function with an output returns a value. We also learned how to use a function with an output.

## Resources

* [Python Functions](https://www.w3schools.com/python/python_functions.asp)

## Assignment

* [Functions with Outputs](https://www.codecademy.com/courses/learn-python/lessons/functions/exercises/functions-with-outputs?action=resume_content_item)


# Exercise 10.1: Functions with Outputs

# Days in Month

## Instructions


In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function `is_leap()` so that instead of printing "Leap year." or "Not leap year." it should **return** `True` if it is a leap year and **return** `False` if it is not a leap year.

You are then going to create a function called `days_in_month()` which will take a **year** and a **month** as inputs, e.g.

```
days_in_month(year=2022, month=2)
```

And it will use this information to work out the **number of days in the month**, then **return** that as the **output**, **e.g.:**

```
28
```

The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

# Hint

1. Look at the function call at the bottom of the code to see the positional arguments.  The order is very important.

2. Feel free to choose your own parameter names.

3. Remember that `month_days` is a List and Lists in Python start at position 0. So the number of days in January is `month_days[0]`

4. Be careful with indentation.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-10-1-test-your-code](https://repl.it/@appbrewery/day-10-1-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 



# Solution

[https://repl.it/@appbrewery/day-10-1-solution](https://repl.it/@appbrewery/day-10-1-solution)


