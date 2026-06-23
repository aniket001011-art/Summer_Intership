sentence = "It's never too late"
visited={}
for i in sentence:
    if i in visited:
        visited[i] += 1
    else:
        visited[i]=0
print((visited))
