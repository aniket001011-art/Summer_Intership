list_1 = [1,2,3,4,5,6,3]
list_2 = [1,2,4,3,7,6,4]
final_list = []
for i in list_1:
    for j in list_2:
        if i == j:
            final_list.append(i)
            break
    else:
        pass 
print(list(set(final_list)))
