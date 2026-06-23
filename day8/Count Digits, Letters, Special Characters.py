str1 = "Python123@!"
count_Digits = 0
count_Letter = 0
count_Special = 0
for i in str1:
    if i.isalpha():
        count_Letter +=1
    elif i.isdigit():
        count_Digits +=1
    else:
        count_Special+=1
print("\nDigites:",count_Digits)
print("Letter:",count_Letter)
print("Special:",count_Special)
        