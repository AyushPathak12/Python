print("Enter first number:")
num1=input()
print("Enter second number:")
num2=input()
    # print("Addition is: ", int(num1)+int(num2))
try:
    print("Addition is: ", int(num1)+int(num2))
except Exception as e:
    print(e)
print("These lines are very important.")
    