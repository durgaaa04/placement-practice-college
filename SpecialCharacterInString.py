s = str(input("Enter the string: "))
def has_special_char(s):
    sc = '!@#$%^&*()-+?_=,<>/'
    for i in s:
        if i in sc:
            return True
    else:
        return False
if has_special_char(s):
    print(f"{s} has special character.")
else:
    print(f"{s} does not have special character.")

