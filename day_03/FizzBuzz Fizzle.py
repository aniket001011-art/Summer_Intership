i=0
for i in range(0,16):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz") 
    elif (i%3==0 or i%5==0):
        print("FizzBuzz")
    else:
        print(i)