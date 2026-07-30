from datetime import datetime

# Decorator
def logger(func):
    def wrapper():
        print("Function Name:", func.__name__)
        print("Called At:", datetime.now())
        func()
    return wrapper

# Function
@logger
def greet():
    print("Hello! Welcome to Python.")

# Function call
greet()