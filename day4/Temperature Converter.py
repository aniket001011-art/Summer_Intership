num=int(input("Enter the value of number--"))

def celsius_to_fahrenheit(celsius):
    q=(celsius * 9/5) + 32
    return q

x=celsius_to_fahrenheit(num)
print("\n convert the number into temperature--",x)