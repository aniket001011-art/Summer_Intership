list1=["apple", "banana", "apple", "cherry", "banana", "apple"]
freq= {}
def count_frequencies(list):
    for i in list:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
print(count_frequencies(list1))