#  Global : can be used anywhere in the file

#  Local : only inside a function 


x = 10 # global

def show():
    y = 5 # local
    print(x + y)
    
show()