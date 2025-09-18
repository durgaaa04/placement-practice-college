def square_elements(numbers):
    mlst = []
    for i in numbers:
        sqr = i ** 2
        mlst.append(sqr)
    print(mlst)

numbers = list(map(int, input("Enter the elements in the list to be squared with space separation: ").split()))
square_elements(numbers)