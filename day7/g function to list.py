h = list(input("Enter the lsit-->"))
def number():
    for i in h:
        yield(i)
x = number()
for j in x:
    print(j)