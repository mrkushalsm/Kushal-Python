file = open("poem.txt", "r")
lines = file.readlines()
for i in lines:
    print(i.replace(" ", "#"))