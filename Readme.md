# Section 8: Day 8: - Beginner - Function Parameters and Caeser Cipher

## Area Calc

# Instructions

You are painting a wall. The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height ✖️ wall width) ÷ coverage per can. 

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 ✖️ 4) ÷ 5 

                         = 1.6

But because you can't buy 0.6 of a can of paint, the **result should be rounded up** to **2** cans. 

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# Example Input

```
test_h = 3
```

```
test_w = 9
```

# Example Output

```
You'll need 6 cans of paint.
```

   

# Hint

**1. To round up a number**: 

[https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python](https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python)

2. Make sure you name your function/parameters the same as when it's called on the last line of code. 

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-8-1-test-your-code](https://repl.it/@appbrewery/day-8-1-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 

# Solution

[https://repl.it/@appbrewery/day-8-1-solution](https://repl.it/@appbrewery/day-8-1-solution)


<hr>



# Prime Numbers

# Instructions

Prime numbers are numbers that can only be cleanly divided by itself and 1. 

[https://en.wikipedia.org/wiki/Prime_number](https://en.wikipedia.org/wiki/Prime_number)


**You need to write a function** that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

 
 ![](https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H)

Here are the numbers up to 100, prime numbers are highlighted in yellow:

![](https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw)

# Example Input 1

```
73
```

# Example Output 1

```
It's a prime number.
```

# Example Input 2

```
75
```

# Example Output 2

```
It's not a prime number.
```

# Hint

1. Remember the modulus: 

[https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python](https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python)

2. Make sure you name your function/parameters the same as when it's called on the last line of code. 

3. Use the same wording as the Example Outputs to make sure the tests pass. 

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-8-2-test-your-code](https://repl.it/@appbrewery/day-8-2-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 


# Solution

[https://repl.it/@appbrewery/day-8-2-solution](https://repl.it/@appbrewery/day-8-2-solution)


<hr>

# Caeser Cipher

# Instructions

You are going to write a program that **encrypts** a message using [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

![](https://cdn.fs.teachablecdn.com/9hKjjdCkRLeCJf2vOUrR)

The encryption works by shifting the letters of the word **forward** in the alphabet by a fixed number.

For example, with a shift of 1, A would become B, B would become C, C would become D, and so on up to **Z** becoming **A**.

![](https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv)

**Important**: The Caesar cipher only encrypts letters. Symbols, such as the space character, should be left as they are. Numbers can be included if you wish.

**Important**: Notice how the letters wrap around the alphabet.

# Example Input 1

```

plain_text = "hello"
```

```
shift = 5
```

```
cipher_text = "mjqqt"
```

# Example Input 2

```
plain_text = "world"
```

```
shift = 3
```

```
cipher_text = "zruog"
```

# Example decode

```python
decode_text = "mjqqt"
```

```
shift = 5
```

```
plain_text = "hello"
```

