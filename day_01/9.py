li =[1,2,34,4,2,2,5,6,45]

visited=[]

for i in li:
    if i not in visited:
        visited.append(i)
    else:
        pass
print(visited)