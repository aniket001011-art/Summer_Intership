string1 = input("Enter the string-->")
words = string1.split()
l= words[0]
for word in words:
    if len(word)>len(l):
        l=word
print(l)
