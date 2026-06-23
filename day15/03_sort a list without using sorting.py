list_1 = [1,3,4,6,2]
for i in range(len(list_1)):
    for j in range(len(list_1)-1-i):
        if list_1[j] > list_1[j+1]:
            list_1[j],list_1[j+1]=list_1[j+1],list_1[j]
print(list_1)

