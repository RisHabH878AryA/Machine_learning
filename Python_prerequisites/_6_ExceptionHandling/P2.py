# Handle division by 0 in a function that takes two numbers.

def divide(a, b):
    return a / b

try:
    print(divide(10,0))
except ZeroDivisionError as e:
    print(e)