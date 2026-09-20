# Parameter: These are the variables listed inside the parentheses in a function definition.
# Argument : These are the actual values that are passed to the function when it is called.
# Positional Arguments: These are the arguments that need to be passed to the function in 
#                       the correct positional order.
# Keyword Arguments: These are the arguments that are passed to the function by explicitly 
#                      specifying the parameter name and its value.

def greet():
    print("Hello ")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()


# Function with input (Parameter & Argument)
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Isn't the weather nice today?")
    
greet_with_name("Vaijinath")



def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}")
    print(f"Isn't the weather nice today in {location}?")

greet_with("Vaijinath", "New York")