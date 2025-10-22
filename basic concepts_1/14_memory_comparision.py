# Value vs Memory comparision

# == check if values are the same 

# is check if both point to the same object in memory


a = [1, 2]
b = [1, 2]
print(a==b)    # True (same values)
print(a is b)  # False (different memory)