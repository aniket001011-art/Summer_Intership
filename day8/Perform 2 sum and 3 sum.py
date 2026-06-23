list1= [1,2,3,4,5,6,9]
# for i in list1:
#     for j in range(i+1,len(list1)):
#         if list1[i] + list1[j] == 9:
#             print(f"{list1[i]} and {list1[j]}")
#         else:
#             pass

for i in range(len(list1)-1):
    if list1[i] + list1[i+1] == 9:
        print(f"\nthe sum of tow value {list1[i]} and {list1[i+1]} is match to the target*9*")
    else:
        pass

for j in range(len(list1)-2):
    if list1[j] + list1[j+1] + list1[j+2] == 12:
        print(f"\nthe sum of three value {list1[j]} + {list1[j+1]} + {list1[j+2]} is match to the target*12*")
    else:
        pass