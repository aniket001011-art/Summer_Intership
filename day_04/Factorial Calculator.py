num=int(input("Enter the value of number--"))
def calculate_factorial(factorial):
    factorial = 1
    for i in range (1,num+1):
        factorial= factorial*i
    return factorial
x=calculate_factorial(num)
print("\n the factorial calculator of give number is--",x)

