dict1 = {}
for i in range(10):
    country = input("Enter country name: ")
    capital = input(f"Enter the capital of {country}: ")
    dict1[country] = capital

for key in dict1:
    if key.startswith("A"):
        print(f"The capital of {key} is", dict1[key])
