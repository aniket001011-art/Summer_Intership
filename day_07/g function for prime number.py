num = int(input("Enter the number-->"))
def number():
    if num>1:
       for i in range (2,num):
          if i%2==0:
            pass
          else:
            yield i
x = number()
for j in x:
    print(j)