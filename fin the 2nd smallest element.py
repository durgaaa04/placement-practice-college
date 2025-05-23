import math
arr = [1, 2, 3, 4, 5]
min = arr[0]
for i in range(len(arr)):
    if min > arr[i]:
        min = arr[i]
min2 = math.inf
for i in range(len(arr)):
    if (arr[i] != min and min2 > arr[i]):
        min2 = arr[i]
print(min2)
