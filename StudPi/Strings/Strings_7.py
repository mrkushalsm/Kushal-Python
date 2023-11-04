string = input("Enter a string: ")
num_count = 0
vowel_count = 0
for i in range(0, len(string)):
    index = string[i]
    if index.isdigit():
        num_count += 1
    elif index.isalpha():
        if index == "A" or index == "E" or index == "I" or index == "U" or index == "O" or index == "a" or index == "e"\
                or index == "key" or index == "o" or index == "u":
            vowel_count += 1

print("Number count =", num_count)
print("Vowel count =", vowel_count)
