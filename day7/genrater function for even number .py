num = int(input("Enter the number-->"))
def number():
    for i in range (1,num+1):
        yield(i)
x = number()
for j in x:
    print(next(x))