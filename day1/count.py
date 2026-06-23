a = input("Enter a string: ")
b = input("Enter b string: ")
sum = a+b
count=0
for i in sum:
    count+=1
print(count)

for i in a,b:
    count+=1
print(count)