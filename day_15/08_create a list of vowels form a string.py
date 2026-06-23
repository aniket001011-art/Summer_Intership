str_1 = input("\nEnter the string...")
str_1 = str_1.lower()
list_1 = []
for i in str_1:
    # if i in ['a','e','i','o','u']:
    # if i in ('a','e','i','o','u'):
    # if i in 'aeiou':
    if i in "aeiou":
        list_1.append(i)
    else:
        pass
print(list(set(list_1)))