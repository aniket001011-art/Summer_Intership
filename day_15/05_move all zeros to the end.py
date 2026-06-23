#move all zeroes to end
#not best approch
list_1 = [0,3,4,0,5,0]
for i in range(len(list_1)):
    for j in range(len(list_1)-1-i):
        if list_1[j] > list_1[j+1]:
            list_1[j],list_1[j+1]=list_1[j+1],list_1[j]
print(list_1)
list_2 = []
for x in range(len(list_1)-1,-1,-1):
    list_2.append(list_1[x])
print(list_2)

#better Approch
list=[0,2,0,0,5,6]
   
for i in range(len(list)):
    for j in range(len(list) - 1 - i):
        if list[j] == 0:
            list[j], list[j + 1] = list[j + 1], list[j]
    else:
        pass
print(list)    