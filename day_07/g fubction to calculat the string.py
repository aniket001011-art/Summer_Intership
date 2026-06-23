num = input("Enter the string-->")
def string():
    for i in num:
        yield(i)
x = string()
for j in x:
    print(j)