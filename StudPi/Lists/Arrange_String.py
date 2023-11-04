string = input("Enter a string: ")
list1 = ['']
list1.clear()
for i in range(0, len(string)):
    list1.append(string[i])

for i in range(0, len(list1)):
    small = list1[i]
    pos = i
    for j in range(i + 1, len(list1)):
        if list1[j].casefold() > small:
            small = list1[j]
            pos = j
    temp = list1[i]
    list1[i] = list1[pos]
    list1[pos] = temp

string_formatted = ""
for i in range(0, len(list1)):
    string_formatted = string_formatted + list1[len(list1) - 1 - i]

print(string_formatted)
