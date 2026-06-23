num = int(input("Enter the number-->"))
def number():
        a=0
        b=1
        for i in range (0,num):
             yield a
             a,b=b,a+b
x = number()
for j in x:
    print(j)