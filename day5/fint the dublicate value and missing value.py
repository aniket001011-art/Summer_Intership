l1 = [1,2,2,4,5]
# find the doublicate value
visited={}
for i in l1:
    if i in visited:
        visited[i]+=1
    else:
        visited[i]=1
print(visited)
for keys,values in visited.items():
    if values > 1:
        print(f"{keys} has dublicate value. it appar {values} times")
    else:
        pass

# find the missing value
num= (int(input("ENter the value--")))
for i in range (1,num+1):
    if i in l1:
        pass
    else:
        print(i)

for i in range (1,6):
    if i in l1:
        pass
    else:
        print(i)