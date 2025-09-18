def remove_space(s):
    rstr = ""
    for i in s:
        if i != " ":
            rstr += i
    print(rstr)

s = str(input("Enter a string: "))
remove_space(s)