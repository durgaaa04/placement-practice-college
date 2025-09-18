def find_min(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

def selection_sort(arr):




if __name__ == '__main__':
    arr = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    print(find_min(arr))
