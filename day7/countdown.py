num = int(input("Enter the number-->"))
def number():
    for i in range (num,0,-1):
        yield i
x = number()
for j in x:
    print(j)