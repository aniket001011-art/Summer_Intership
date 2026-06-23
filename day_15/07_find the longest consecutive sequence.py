arr = [100,4,102,1,3,2,0,101 ] 
# Bubble Sort
n = len(arr)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
# print("Sorted Array:", arr)
y = sorted(arr)
print(y)
longest = 1
current = 1
 
for i in range(1, n):
    if y[i] == y[i - 1] + 1:
        current += 1
    else:
        if current > longest:
            longest = current
        current = 1
 
if current > longest:
    longest = current
 
print("Longest Consecutive Sequence Length:", longest)