"""decimal = int(input("Enter a decimal number: "))
quotient = decimal
binary = ""
while quotient != 0:
    remainder = quotient % 2
    quotient = quotient // 2
    binary = str(remainder) + binary

print("Binary value of", decimal, "is", binary)"""

menu_dict = {"starters": {1: {"Spring Rolls": {"Price": 100, "Quantity": 0}},
                          2: {"French Onion Soup": {"Price": 100, "Quantity": 0}},
                          3: {"Tomato Bruschetta": {"Price": 100, "Quantity": 0}},
                          4: {"Caesar Salad": {"Price": 100, "Quantity": 0}}}}
print(menu_dict["starters"][1]["Spring Rolls"]["Quantity"])