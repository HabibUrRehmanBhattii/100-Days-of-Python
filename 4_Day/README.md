41. Random Module

42. [Interactive Coding Exercise] Heads or Tails

# Day 4 - Intermediate - Randomisation and Python Lists

## 41. Random Module

The random module is a built-in module in Python that allows us to generate random numbers. We can use it to generate random numbers, random floating point numbers, random decimals, random choices from a list, and more.

To use the random module, we need to import it at the top of our file.

```python
import random
```

### 41.1. Random Integers

To generate a random integer, we can use the `randint()` function. This function takes two parameters, a starting number and an ending number. It will return a random integer between the two numbers, including the starting and ending numbers.

```python
import random

random_integer = random.randint(1, 10)
print(random_integer)
```

### 41.2. Random Floats

To generate a random floating point number, we can use the `random()` function. This function will return a random floating point number between 0 and 1.

```python
import random

random_float = random.random()
print(random_float)
```

### 41.3. Random Decimals

To generate a random decimal number, we can use the `randrange()` function. This function takes three parameters, a starting number, an ending number, and a step. It will return a random number between the starting and ending numbers, including the starting and ending numbers, and with the step between each number.

```python
import random

random_float = random.randrange(0, 5, 0.5)
print(random_float)
```

### 41.4. Random Choices

To generate a random choice from a list, we can use the `choice()` function. This function takes a list as a parameter and will return a random element from that list.

```python
import random

fruits = ["Apple", "Pear", "Orange"]
random_fruit = random.choice(fruits)
print(random_fruit)
```

### 41.5. Random Choices with Weighting

To generate a random choice from a list with weighting, we can use the `choices()` function. This function takes two parameters, a list and a list of weights. It will return a random element from the list, with the weighting of each element determined by the weights list.

```python
import random

fruits = ["Apple", "Pear", "Orange"]
weights = [1, 2, 3]
random_fruit = random.choices(fruits, weights=weights)
print(random_fruit)
```

### 41.6. Random Choices with Weighting and K

To generate multiple random choices from a list with weighting, we can use the `choices()` function. This function takes three parameters, a list, a list of weights, and a number of choices to make. It will return a list of random elements from the list, with the weighting of each element determined by the weights list.

```python
import random

fruits = ["Apple", "Pear", "Orange"]
weights = [1, 2, 3]
random_fruit = random.choices(fruits, weights=weights, k=10)
print(random_fruit)
```

### 41.7. Random Choices with K

To generate multiple random choices from a list, we can use the `choices()` function. This function takes two parameters, a list and a number of choices to make. It will return a list of random elements from the list.

```python
import random

fruits = ["Apple", "Pear", "Orange"]
random_fruit = random.choices(fruits, k=10)
print(random_fruit)
```

### 41.8. Random Choices without Replacement

To generate multiple random choices from a list without replacement, we can use the `sample()` function. This function takes two parameters, a list and a number of choices to make. It will return a list of random elements from the list, without replacement.

```python
import random

fruits = ["Apple", "Pear", "Orange"]
random_fruit = random.sample(fruits, k=10)
print(random_fruit)
```

## 42. [Interactive Coding Exercise] Heads or Tails

## Heads or Tails

# Instructions

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 

**Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g.
1 means Heads
0 means Tails 

# Example Output

```
Heads
```

or

```
Tails
```


# Solution

[https://repl.it/@appbrewery/day-4-1-solution](https://repl.it/@appbrewery/day-4-1-solution)


## 43. Understanding the Offset and Appending Items to Lists

In this lesson, we will learn how to use the offset to access items in a list. We will also learn how to append items to a list. 







# 44. [Interactive Coding Exercise] Banker Roulette - Who will pay the bill?

## Banker Roulette - Who will pay the bill?

# Who's Paying

## Instructions

You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill. 

**Important**: You are not allowed to use the `choice()` function.

**Line 8** splits the string `names_string` into individual names and puts them inside a **List** called `names`. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# Example Input

```
Angela, Ben, Jenny, Michael, Chloe
```
Note: notice that there is a space between the comma and the next name. 
# Example Output

```
Michael is going to buy the meal today!
```


# Hint

1. You might need the help of the `len()` function.   

[https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list](https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list)

2. Remember that Lists start at index 0!

# Solution

[https://repl.it/@appbrewery/day-4-2-solution](https://repl.it/@appbrewery/day-4-2-solution)

# 46. [Interactive Coding Exercise] Treasure Map

## Treasure Map

# Instructions

You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called ```map```.

This ```map``` contains a nested list.
When ```map``` is printed this is what the nested list looks like:
```
['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
```
In the starting code, we have used new lines (```\n```) to format the three rows into a square, like this:
```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```
This is to try and simulate the coordinates on a real map. 

![](https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1440,f_auto/Co-ordinates_oggjzg.jpg)

Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

![](https://cdn.fs.teachablecdn.com/2vnboIYTFFruvl9FJ2w5)

First your program must take the user input and convert it to a usable format. 

Next, you need to use it to update your nested list with an "x". 

# Example Input 1

column 2, row 3 would be entered as:

```
23
```

# Example Output 1

```
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', 'X', '⬜️']
```

# Example Input 2

column 3, row 1 would be entered as:

```
31
```

# Example Output 2

```
['⬜️', '⬜️', 'X']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
```

e.g. When you hit **run**, this is what should happen: 

![](https://cdn.fs.teachablecdn.com/5hliFjyIR96LdestyfPd)

# Hint

1. Remember that Lists start at index 0!
2. ```map``` is just a variable that contains a nested list. It's not related to the map function in Python.

# Solution

[https://repl.it/@appbrewery/day-4-3-solution](https://repl.it/@appbrewery/day-4-3-solution)

# 47. Day 4 Project: Rock Paper Scissors

## Rock Paper Scissors

# Instructions

Make a rock, paper, scissors game. 

Inside the `main.py` file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: `rock`, `paper`, and `scissors`. This will make it easy to print them out to the console. 

Start the game by asking the player:

*"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

From there you will need to figure out: 
* How you will store the user's input.
* How you will generate a random choice for the computer.
* How you will compare the user's and the computer's choice to determine the winner (or a draw).
* And also how you will give feedback to the player. 

You can find the "official" rules of the game on [the World Rock Paper Scissors Association website.](https://wrpsa.com/the-official-rules-of-rock-paper-scissors/)


# Solution

[https://replit.com/@appbrewery/rock-paper-scissors-end](https://replit.com/@appbrewery/rock-paper-scissors-end)
