str=input("Enter the string:")
str=str[::-1]
print(str)

str1=input("Enter the firststring1:")
str2=input("Enter the second string:")
print(str1[::-1])
print(str1==str2)

if str1[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palinderome")