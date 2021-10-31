a=int(input("ENTER FIRST NUMBER: "))
b=int(input("ENTER SECOND NUMBER: "))
c= sum((a,b))  # Built in function
print(c)

def funcname1(a,b):
    print("Hello you are in function1", a+b)
#function1(a,b)
def function2(a,b):
    """This is a function which will calculatethe average of the two numbers. This function does not work for docstring... Ha Ha Ha..."""   #This is a Docstring
    average=(a+b)/2
    # print(average)
    return average
v=function2(a,b)
print(v)
print(function2.__doc__)     #To print the docstrings...
