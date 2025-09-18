def first_recurring_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

s = str(input("Enter a string:"))
print(first_recurring_char(s))