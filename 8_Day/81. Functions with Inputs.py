# Review: 

# def greet():
#     print("Hello"),
#     print("How do you do?"),
#     print("Isn't the weather nice today?")
# greet()

# RESULT
# """ Here is the explanation for the code above:
# 1. We use the keyword def to define a function. This is followed by the function name and parentheses ().
# 2. The code to be executed is placed within these parentheses.
# 3. The code is indented.
# 4. We have also defined a new function, greet(), which prints a friendly greeting. 
# 5. We then call the function, greet(), which executes the code within the function. """


# Functions with Inputs 

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"Isn't the weather nice today {name}?")
# greet_with_name("John")

# """ Here is the explanation for the code above:
# 1. First, we define a function called greet_with_name. This function has one parameter, which is name.
# 2. Then, we print a greeting message using the name variable.
# 3. Then, we print a question using the name variable.
# 4. Then, we print a statement using the name variable.
# 5. Finally, we call the function and pass in "John" as an argument. """


# ## Multiple Parameters

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}?")
    
# greet_with("john", "london")

greet_with(location="london", name="john")