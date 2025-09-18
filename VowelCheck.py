def vowel_check(s):
    vowel_lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels = []
    for i in s:
        if i in vowel_lst:
            vowels.append(i)
    print(vowels)

s = str(input("Enter the string: "))
vowel_check(s)