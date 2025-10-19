#  Used to pass variable number of arguments

def show(*args, **kwargs):
    print(args)
    print(kwargs)
    
show(1, 2, 3, name= "shinchan", age= 22)