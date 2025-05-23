arr = [5, 3, 4, 2]
s = 0
e = len(arr) - 1
while (s < e):
    temp = arr[s]
    arr[s] = arr[e]
    arr[e] = temp
    s += 1
    e -= 1
print(arr)