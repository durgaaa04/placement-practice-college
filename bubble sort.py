#ascending
arr = [5, 3, 4, 2]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)

#descending
arr = [5, 3, 4, 2]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)

#1st half ascending 2nd half descending
arr = [1, 3, 2, 6, 8, 7]
for i in range(len(arr) // 2):
    for j in range(i + 1, len(arr) // 2 ):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
for i in range(len(arr) // 2, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)