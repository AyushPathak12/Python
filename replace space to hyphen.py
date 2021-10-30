str = input("Enter a string:")
n = len(str)
for i in range(n):
    if (str[i] == " "):
        str = str.replace(str[i], '-')
        break
    else:
        print("Entered string has no spaces !!!.. \n Aborting \n Please enter the correct string to find the result")
        break

print("New string is:")
print(str)
