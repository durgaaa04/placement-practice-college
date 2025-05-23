# def count1(arr, n):
#     visited = [False for i in range(n)]
#     for i in range(n):
#         if(visited[i] == True):
#             continue
#         count = 1
#         for j in range(i + 1, n, 1):
#             if arr[i] == arr[j]:
#                 visited[j] = True
#                 count += 1
#         print(arr[i], count)
# arr = [1, 2, 3, 4, 4]
# n = len(arr)
# count1(arr, n)

#alternate method
def freq(lst):
    counts = {}
    for i in lst:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1 
    
    for key, value in counts.items():
        print(f"{key} {value}")

lst = list(map(int, input("enter the elements with space separation: ").split()))
freq(lst)


