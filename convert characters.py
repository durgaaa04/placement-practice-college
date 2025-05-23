str = "dEEksHa"
str1 = []
for i in str:
    if i.isupper():
        str1.append(i.lower())
    elif i.islower():
        str1.append(i.upper())
    else:
        str1.append(i)
print("".join(str1))