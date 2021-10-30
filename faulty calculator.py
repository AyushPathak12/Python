# Faulty Calculator Program
# 56+9=77
# 45*3=555
# 56/6=4
val1 = float(input("Enter your first  number:"))
val2 = float(input("Enter your second number:"))
op = input("Enter a operator \n + \n - \n * \n %\n ")
if op == "+":
    if val1 == 56 and val2 == 9:
        print("Addition is =", 77)
    else:
        print("Addition is =", val1+val2)

elif op == "-":
    print("Subtaction is =", val1-val2)
elif op == "*":
    if val1 == 45 and val2 == 3:
        print("Multiplication is =", 555)
    else:
        print("Multiplication is =", val1*val2)
elif op == "%":
    if val1 == 56 and val2 == 6:
        print("Division is =", 4)
    else:
        print("Division is =", val1/val2)

else:
    print("Error Please give a right operator")
