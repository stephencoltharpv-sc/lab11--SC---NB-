# https://github.com/stephencoltharpv-sc/lab11--SC---NB-
# Partner 1: Stephen Coltharp
# Partner 2: Nishchay Bhattarai
import math
def square_root(a):
    if a <0:
        raise ValueError("Invalid square root")
    return math.sqrt(a)# raise ValueError if a < 0

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b
def div(a,b):
    if a==0:
        raise ZeroDivisionError("division by zero")
    return b/a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b


