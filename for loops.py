# list1=["Hastty", "Larry", "Carry"]
# list1=("Hastty", "Larry", "Carry")
list1=[["Hastty", 1], ["Larry", 2], ["Carry", 6]]
dict1=dict(list1)
# print(dict1)
# for item, lollypop in dict1.items():
#     print(item, "eats",  lollypop,"Lollypop")

# for item in dict1:
#     print(item)

items=(int,float, "Harry",5,6,87,56,76)

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)