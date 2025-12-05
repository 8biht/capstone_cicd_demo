import math

def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b

def log (a):
    return math.log(a)

def square (a):
    return a * a

def sin (a):
    return math.sin(a)

def cos (a):
    return math.cos(a)

def square_root (a):
    if a / abs(a) == -1:
        print("Cannot take the square root of a negative number.")
        return None
    return math.sqrt(a)

def percentage (a, b):
    if a / abs(a) == -1:
        print("Cannot have a negative percentage.")
        return None
    return (a / b ) * 100
