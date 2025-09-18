def substring_finder(s, sub_s):
    if sub_s in s:
        print(f"{sub_s} is in {s}.")
    else:
        print(f"{sub_s} is not in {s}.")

s = str(input("Enter a string: "))
sub_s = str(input("Enter the substring to be checked: "))
substring_finder(s, sub_s)