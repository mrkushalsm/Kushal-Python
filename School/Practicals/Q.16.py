unit = int(input("Enter your units: "))

if unit <= 100:
    bill = unit * 3.46
elif unit >= 101 and unit <= 300:
    bill = 346 + ((unit - 100) * 7.43)
elif unit >= 301 and unit <= 500:
    bill = 346 + 1486 + ((unit - 300) (  10.32))
else:
    bill = 346 + 1486 + 2064 + ((unit - 500) * 11.71)

print("Bill per unit:", bill)
bill += (unit * 1.45)
print("Bill after adding line rent:", bill)
bill += 100
print("Bill after adding meter rent:", bill)
bill += (bill * 0.16)
print("total bill after adding tax:", bill)
