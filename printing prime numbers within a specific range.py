print("enter a positive integer !!!")
n1 = int(input("enter number 1:"))
n2 = int(input("enter number 2:"))
prime_nums = []
for i in range(n1, n2+1):
    if(i > 1):
        flag = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                flag = 1
        if (flag != 1):
            prime_nums.append(i) 
print(prime_nums)
    
    