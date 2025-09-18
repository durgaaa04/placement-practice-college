def check_anagram(str1, str2):
    if len(str1) != len(str2):
        print("Not anagrams as they have unequal lengths.")
    else:
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)
        if sorted_str1 == sorted_str2:
            print("strings are anagrams.")
        else:
            print("strings are not anagrams.")

str1 = str(input("Enter string 1: "))
str2 = str(input("Enter string 2: "))
check_anagram(str1, str2)