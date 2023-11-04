string = input("Enter a string: ")
string2 = ""
length = len(string)
for i in range(0, length):
    string2 += str(string[length - 1 - i])
print("Reverse String:", string2)
