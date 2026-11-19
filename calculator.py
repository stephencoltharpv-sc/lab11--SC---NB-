"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a ==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b/a

def logarithm(a, b):
    if b<=0 or a<=0 or b==1:
        raise ValueError("Invalid logarithm")
    return math.log(a,b)

def exponent(a, b):
    return a**b


