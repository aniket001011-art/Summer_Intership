a= [1,2,3,4]
b= [3,4,5,6]
common_elements=[]
for i in a:
    for j in b:
        if i == j:
            common_elements.append(i)
        else:
            pass
print(common_elements)
