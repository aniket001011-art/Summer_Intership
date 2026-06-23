list_1 = [1,3,2,4,3,3,3,5,3]
total_majortiy= len(list_1)/2
print(total_majortiy)
freq = {}
for i in list_1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
for key,values in freq.items():
    if values >= total_majortiy:
        print("majortiy element..",key)
    else:
        pass