num = int(input("Enter the number-->"))
def number():
    for i in range (2,num):
        yield i**2
x = number()
for j in x:
    print(j)