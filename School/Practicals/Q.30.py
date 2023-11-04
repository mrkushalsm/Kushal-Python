import pickle
dict1 = {}
n = int(input("Enter a number: "))
for i in range(n):
    roll_no = input("Enter the Roll no.: ")
    name = input("Enter the name: ")
    marks = input("Enter the marks: ")
    dict1[roll_no] = [name, marks]
    ch = input("Do you want to add more data (Y/N or y/n): ")
    if ch in "Nn":
        break
f = open("hello.bin", "wb")
pickle.dump(dict, f)
f.close()
