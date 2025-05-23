string = "hello"
vowels = ['a', 'e', 'i', 'o', 'u']
str1 = ""
for i in range(len(string)):
    if string[i] not in vowels:
        str1 += string[i]
print(str1)