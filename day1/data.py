data= [1,2,3,1,2,2,3,4]
visited={}
for num in data:
    if num in visited:
        visited[num]+= 1
    else:
        visited[num]=1
print(visited)