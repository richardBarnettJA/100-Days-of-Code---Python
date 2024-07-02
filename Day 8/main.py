# Functions with Parameters
def greet(name):
    print("Hello", name)
    print("Great to see you", name)
    print(f"How are you {name}?")

greet("Bob")

# some = 123
# some is the parameter and 123 is the argument


# Positional arguments
def greet(name, location, size):
    print(f"Hello {name}. You are in {location} and are a size {size}.")

greet(location = "Jamaica", size = "large", name = "Bob")