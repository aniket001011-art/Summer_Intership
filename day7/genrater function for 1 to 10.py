def number():
    for i in range (1,11):
        yield(i)
x = number()
for j in x:
    print(j)