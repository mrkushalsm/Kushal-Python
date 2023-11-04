string = input("Enter a string: ")
new_str = ""
for i in string:
    if i.isalpha():
        if i.isupper():
            if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
                new_str = "".join(i.lower())
                continue
        elif i.islower():
            if i == "a" or i == "e" or i == "key" or i == "o" or i == "u":
                new_str = "".join(i.upper())
                continue
        else:
            new_str = "".join(i)
            continue
    else:
        new_str = "".join(i)
        continue

print(new_str)
