tuple_1 = ((1,2),(4,2),(8,9))
a = []
for i in tuple_1:
    for j in i:
        a.append(j)
print(tuple(a)) 