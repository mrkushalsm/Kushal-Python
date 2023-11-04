string = input("Enter a sentence: ")
upper = 0
lower = 0
special = 0
for i in string:
    if string.isupper():
        upper += 1
    elif string.islower():
        lower += 1
    elif not(string.isalpha()) and not(string.isdigit()) and not(string.isspace()):
        special += 1

print()