# Decorator to check positive integers
def validate(func):
    def wrapper(*args):
        for i in args:
            if type(i) != int or i <= 0:
                print("Error! Enter only positive integers.")
                return
        func(*args)
    return wrapper

@validate
def add(a, b):
    print("Sum =", a + b)

# Function calls
add(10, 20)
add(-5, 10)
add(10, "5")