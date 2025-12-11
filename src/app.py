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
    if (a >= 0):
        return math.sqrt(a)
    else:
        return "invalid"

def percentage (a, b):
    if ((a / abs(a)) == -1) or (b == 0):
        return "invalid"
    else:
        return ((a / b ) * 100)
