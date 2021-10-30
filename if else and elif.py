# var1=6
# var2=56
# var3= int(input())
# if var3>var2:
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser")

# l1=[5,7,3]
# if 5 in l1:
#     print("Yes in list")
# if  15 not in l1:
#     print("Not in list")

age = int(input("What is your age:\n"))
if age > 7 and age < 100:
    if age > 18:
        print("You are able to drive.")
    elif age == 18:
        print("We can't decide.Come Physically. ")
    else:
        print("You are not able to drive.")
else:
    print("Not a valid age")
