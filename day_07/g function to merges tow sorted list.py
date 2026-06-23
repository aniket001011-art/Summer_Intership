list1 = list(input("Enter the list1....."))
list2 = list(input("Enter the list2....."))
def merges_list():
    a = list1.extend(list2)
    yield list1
x = merges_list()
for j in x:
    print(j)