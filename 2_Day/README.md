# Day 2

## Part 1
Instructions

Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

Example Input
39
Example Output
3 + 9 = 12
12

Hint
Try to find out the data type of two_digit_number.
Think about what you learnt about subscripting.
Think about type conversion.

[Solution](https://repl.it/@appbrewery/day-2-1-solution)

## Part 2
Instructions
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

![](https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv)

Warning you should convert the result to a whole number.

Example Input
```
weight = 80
height = 1.75
```
Example Output
```
80 ÷ (1.75 x 1.75) =  26.122448979591837
26
```
![](https://cdn.fs.teachablecdn.com/wmjVjddeSmGj0QVtOUrE)

Hint
1. Check the data type of the inputs.
2. Try to use the exponent operator in your code.
3. Remember PEMDAS.
4. Remember to convert your result to a whole number (int).

[Solution](https://repl.it/@appbrewery/day-2-2-solution)


## Part 3

Instructions
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input
```
56
```
Example Output
```
You have 12410 days, 1768 weeks, and 408 months left.
```
e.g. When you hit run, this is what should happen:

![](https://cdn.fs.teachablecdn.com/RjqBViZQpyVTv7XY6cfA)

Hint
1. There are 365 days in a year, 52 weeks in a year and 12 months in a year.
2. Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.

[Solution](https://repl.it/@appbrewery/day-2-3-solution)

## Main Project - Tip Calculator

Instructions
In this you will make a tip calculator. It will work out the total amount for a bill including the tip.

## Important

**You should try to complete this project without using the help of the hints. But if you get stuck on a particular part of the project, then you can check the hints.**

tip is in percentage


**Example Input**
```
total_bill = 124.56
tip = 12
split = 7
```

**Example Output**
```
Each person should pay: 19.93
```

**Hint**
1. There are 2 ways to round a number. You might have to do some Googling to solve this.💪
2. Try Googling the Python modulo operator.

[Solution](https://repl.it/@appbrewery/day-2-4-solution)

