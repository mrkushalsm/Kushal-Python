ename = input("Enter empolyee name: ")
sal = int(input("Enter base salary: "))

if sal >= 10000:
    bs = int(sal * 5 / 100)
else:
    bs = int(sal * 3 / 100)

ts = sal + bs
print("Employee name: ", ename)
print("Salary: {}, Bonus: {}, Total salary: {}".format(sal, bs, ts))
