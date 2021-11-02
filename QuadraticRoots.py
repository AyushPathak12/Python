import math
choice='y'
while choice=='y' or choice=='Y':
    print("For quadratic equation, ax**2+bx+c=0, enter coefficients below")
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=int(input("Enter c:"))
    delta=b*b-4*a*c

    if a==0:
        print("Value of", a, 'should not be zero')
        print("\n Aborting!!!!!!")
    else:
        if delta>0:
            root1=(-b+math.sqrt(delta))/(2*a)
            root2=(-b-math.sqrt(delta))/(2*a)
            print("Roots are REAL and UNEQUAL",(root1, root2))
            
        elif delta==0:
            root1=-b/(2*a)
            root2=-b/(2*a)
            print("Roots are REAL and EQUAL",(root1, root2))
            
        else:
            root1 = root2 = -b / (2 * a)
            imaginary = math.sqrt(-delta) / (2 * a)
            print("Roots are COMPLEX and IMAGINARY",(root1, imaginary, root2, imaginary))   
        choice=input("Press y to continue else press any other key.")
