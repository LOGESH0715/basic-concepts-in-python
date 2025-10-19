# Recursion in python

# function calling itself

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

print(factorial(5))
