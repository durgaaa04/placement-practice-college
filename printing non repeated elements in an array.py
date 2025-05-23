def freq(lst):
    counts = {}
    non_repeated = []
    for i in lst:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1 
    
    for key, value in counts.items():
        if value == 1:
            non_repeated.append(key)
    
    for j in non_repeated:
        print(j)

lst = list(map(int, input("enter the elements with space separation: ").split()))
freq(lst)