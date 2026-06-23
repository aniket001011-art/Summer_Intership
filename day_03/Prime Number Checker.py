num = int(input("Enter the number to check the prime number--"))
if num>1:
      for i in range(2,num):
           if (num%2==0):
               print("it is not a prime")
               break
           else:
               print("it is a prime.")
               break
else:
     print("it is a prime.")