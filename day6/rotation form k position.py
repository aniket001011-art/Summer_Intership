# def uniqye(aa):
#    visited = []
#    for i in aa:
#       if i in visited:
#           visited(i)=1
#       else:
#           visited(i)+=1

# A = list(input("Enter the list elements dta -->"))
# a = uniqye(A)
# print(a)
def filter_unique(data):
   visited = {}
   for i in data:
      if i in visited:
          visited[i]+=1
      else:
         visited[i]=1 
data1 = [1,2,3,4,5,3,4]
a =filter_unique(data1)
print(a)