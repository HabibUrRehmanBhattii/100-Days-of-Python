# Section 9 : Day 9-Beginner-Dictionaries, Nesting, and the Secret Auction

## Dictionaries

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is unordered, changeable and does not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

You can access the items of a dictionary by referring to its key name, inside square brackets:

```python
x = thisdict["model"]
```

There is also a method called get() that will give you the same result:

```python
x = thisdict.get("model")
```

## Change Values

You can change the value of a specific item by referring to its key name:

```python
thisdict["year"] = 2018
```

## Loop Through a Dictionary

You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

```python
for x in thisdict:
  print(x)
```

## Nesting

Nesting is the process of putting data structures within data structures, such as a list that contains dictionaries.

```python
# A list of dictionaries
student_scores = [
  {"student": "Angela", "score": 90},
  {"student": "James", "score": 56},
  {"student": "Lily", "score": 77}
]
```

## The Secret Auction

You are going to write a program that will add to a secret auction program.

There are two possible paths: the bidder can type "yes" or "no". If they type "yes" then they will be asked for the name and the bid. If they type "no" then the program should print out the highest bidder.

```python
#HINT: You can call clear() to clear the output in the console.
from replit import clear
#HINT: You can use the max() function to get the highest number from a list.
# Example List
# auction_data = []
# auction_data.append({"name": "Angela", "bid": 123})
# auction_data.append({"name": "James", "bid": 321})
# auction_data.append({"name": "Jenny", "bid": 222})
# highest_bid = 0
# winner = ""
# for bidder in auction_data:
#   bid_amount = bidder["bid"]
#   if bid_amount > highest_bid:
#     highest_bid = bid_amount
#     winner = bidder["name"]
# print(f"The winner is {winner} with a bid of ${highest_bid}")
```

## Solution

```python
from replit import clear
#HINT: You can call clear() to clear the output in the console.
#HINT: You can use the max() function to get the highest number from a list.
# Example List
# auction_data = []
# auction_data.append({"name": "Angela", "bid": 123})
# auction_data.append({"name": "James", "bid": 321})
# auction_data.append({"name": "Jenny", "bid": 222})
# highest_bid = 0
# winner = ""
# for bidder in auction_data:
#   bid_amount = bidder["bid"]
#   if bid_amount > highest_bid:
#     highest_bid = bid_amount
#     winner = bidder["name"]
# print(f"The winner is {winner} with a bid of ${highest_bid}")
print("Welcome to the secret auction program.")
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
 ```




# Grading Program

## Instructions

You have access to a database of `student_scores` in the format of a dictionary. The **keys** in `student_scores` are the **names** of the students and the **values** are their exam **scores**. 

Write a program that **converts their scores to grades**. By the end of your program, you should have a new dictionary called `student_grades` that should contain student **names** for **keys** and their **grades** for **values**. T**he final version** of the `student_grades` dictionary will be checked. 

**DO NOT** modify lines 1-7 to change the existing `student_scores` dictionary. 

**DO NOT** write any print statements.

This is the scoring criteria:

> Scores 91 - 100: Grade = "Outstanding"

> Scores 81 - 90: Grade = "Exceeds Expectations"

> Scores 71 - 80: Grade = "Acceptable"

> Scores 70 or lower: Grade = "Fail"

# Expected Output

```
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
```

# Hint

1. Remember that looping through a Dictionary will only give you the **keys** and not the values. 

2. If in doubt as to why your code is not doing what you expected, you can always print out the intermediate values. 

3. At the **end** of your program, the print statement will show the final `student_scores` dictionary, do not change this.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-9-1-test-your-code](https://repl.it/@appbrewery/day-9-1-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 


# Solution

[https://repl.it/@appbrewery/day-9-1-solution](https://repl.it/@appbrewery/day-9-1-solution)



# Dictionary in List

## Instructions

You are going to write a program that adds to a `travel_log`. You can see a travel_log which is a **List** that contains 2 **Dictionaries**. 

Write a function that will work with the following line of code on line 21 to add the entry for Russia to the `travel_log`. 

```
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
```

> `You've visited Russia 2 times.`

> `You've been to Moscow and Saint Petersburg.`

**DO NOT** modify the `travel_log` directly. You need to create a function that modifies it. 

# Hint

1. Look at the function call above to see what the name of the function should be.

2. The inputs for the function are positional arguments. The order is very important.

3. Feel free to choose your own parameter names.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-9-2-test-your-code](https://repl.it/@appbrewery/day-9-2-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 


# Solution

[https://repl.it/@appbrewery/day-9-2-solution](https://repl.it/@appbrewery/day-9-2-solution)


