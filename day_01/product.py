num=int(input("enter numbers:"))
prod=1
if num==1:
    prod=1
else:
    while num!=0:
        digit=num%10
        prod=prod*digit
        num = num//10
        print(prod)
print("Number of digits:", prod)