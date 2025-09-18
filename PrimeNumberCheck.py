n = int(input("Enter a positive integer to check whether its prime or not: "))
if n < 2:
    print(f"{n} is not a prime number.")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            break
    else:
        print(f"{n} is a prime number.")