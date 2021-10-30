a=9
b=8
c= sum((a,b))  # Built in function
print(c)

def funcname1(a,b):
    print("Hello you are in function1", a+b)
# funcname1(5,7)
def function2(a,b):
    """This is a function which will calculatethe average of the two numbers. This function does not work for docstring... Ha Ha Ha..."""   #This is a Docstring
    average=(a+b)/2
    # print(average)
    return average
v=function2(5,7)
print(v)

print(function2.__doc__)     #To print the docstrings...