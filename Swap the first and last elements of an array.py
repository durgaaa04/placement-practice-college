def swap_elements(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    print("After swapping 1st element with last element:", arr)

arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
swap_elements(arr)