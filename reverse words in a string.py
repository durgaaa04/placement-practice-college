def words_reversed(s):
    words = s.split(" ")[::-1]
    rstr = ""
    for i in words:
        rwords = i[::-1]
        rstr += rwords + " "
    print(rstr.strip())

s = input("Enter a string whose words need to be reversed: ")
words_reversed(s)