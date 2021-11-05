A=input("ENTER ANYTHING: ")
B=input("ENTER ANYTHING: ")
C=input("ENTER ANYTHING: ")

E= A.lower()
F= B.lower()
G= C.lower()

Data = [E, F, G]
for i in range(len(Data)):
    if (Data[i].islower()):
        Data[i]=Data[i].upper()

print(Data)
