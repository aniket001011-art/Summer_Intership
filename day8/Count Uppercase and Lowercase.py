str1 = "PyThOn"
count_upper = 0
count_lower = 0
for i in str1:
    if i == i.upper():
        count_upper += 1
    else:
        count_lower +=1
print("\nUpperCase=",count_upper)
print("LowerCase=",count_lower)

