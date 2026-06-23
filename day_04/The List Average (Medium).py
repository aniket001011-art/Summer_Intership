numbers_list = list(map(int,input("Enter the value of list--").split()))

def calculate_average(numver_list):
    x=sum(numbers_list) / len(numbers_list)
    return x

final=calculate_average(numbers_list)
print("\n The average of given values are--",final)


