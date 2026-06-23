data= [1,2,3,2,3,4,5]

visited={}
for num in data:
    if num in visited:
        visited[num] += 1
    else:
        visited[num]=0
print(visited)

