import csv

""" file = open("file_handling.txt", "w")
list1 = ["Meg \n", "Riya \n", "Nair \n", "SG"]
file.writelines(list1)
file.close() """

""" file = open("file_handling.txt", "r")
print(file.readlines(1))
file.close() """

""" file2 = open("file_handling.csv", "a+")
writer = csv.writer(file2)
writer.writerow(["Rollno", "Name", "Marks"])
file2.close() """

file3 = open("file_handling.csv", "r")
reader =  csv.reader(file3)
for rec in reader:
    print(rec)
file3.close()