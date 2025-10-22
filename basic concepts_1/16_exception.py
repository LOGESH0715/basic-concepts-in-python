# Error control

# Handle unexpected errors using (try, except and finally)

try:
    result = 10/0
    
except ZeroDivisionError:
    print("Cannot divide by zero")
    
finally:
    print("done")