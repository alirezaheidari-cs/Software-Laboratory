# arithmetic.py

def add(x, y):
    x = int(x)
    y = int(y)
    return x + y

def subtract(x, y):
    x = int(x)
    y = int(y)
    return x - y

def multiply(x, y):
    x = int(x)
    y = int(y)
    return x * y

def divide(x, y):
    x = int(x)
    y = int(y)
    if y == 0:
        return "Division by zero is not allowed"
    return x / y
