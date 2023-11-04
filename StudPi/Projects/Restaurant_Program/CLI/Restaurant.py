menu_dict = {"starters": {1: {"Spring Rolls": {"Price": 100, "Quantity": 0}},
                          2: {"French Onion Soup": {"Price": 100, "Quantity": 0}},
                          3: {"Tomato Bruschetta": {"Price": 100, "Quantity": 0}},
                          4: {"Caesar Salad": {"Price": 100, "Quantity": 0}}},

             "main_course": {1: {"Grilled Salmon with Dilled Sauce": {"Price": 100, "Quantity": 0}},
                             2: {"Roast Beef with Vegetables": {"Price": 100, "Quantity": 0}},
                             3: {"Chicken and Mushroom Pie": {"Price": 100, "Quantity": 0}},
                             4: {"MarraKesh Vegetarian Curry": {"Price": 100, "Quantity": 0}},
                             5: {"Eggplant Lasagne": {"Price": 100, "Quantity": 0}}},

             "desserts": {1: {"Apple Pie with Cream": {"Price": 100, "Quantity": 0}},
                          2: {"Lemon Meringue Pie": {"Price": 100, "Quantity": 0}},
                          3: {"Vanilla Ice Cream": {"Price": 100, "Quantity": 0}},
                          4: {"Crêpe Suzette": {"Price": 100, "Quantity": 0}},
                          5: {"Fruit Salad": {"Price": 100, "Quantity": 0}}}}

"""
starters = {1: "Spring Rolls", 2: "French Onion Soup", 3: "Tomato Bruschetta", 4: "Caesar Salad"}
main_course = {1: "Grilled Salmon with Dilled Sauce", 2: "Roast Beef with Vegetables", 3: "Chicken and Mushroom Pie",
               4: "MarraKesh Vegetarian Curry", 5: "Eggplant Lasagne"}
desserts = {1: "Apple Pie with Cream", 2: "Lemon Meringue Pie", 3: "Vanilla Ice Cream", 4: "Crêpe Suzette",
            5: "Fruit Salad"}
"""

amount = 0


def menu():
    print("================MENU================")
    print("1. Starters")
    print("2. Main Course")
    print("3. Desserts")
    print("0. Quit menu and print the bill")
    print("====================================")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        starters()
    elif choice == 2:
        main_course()
    elif choice == 3:
        desserts()
    elif choice == 0:
        bill_print()


def starters():
    print("=================STARTERS=================")
    print("1. Spring Rolls")
    print("2. French Onion Soup")
    print("3. Tomato Bruschetta")
    print("4. Caesar Salad")
    print("0. Go back to Main Menu")
    print("==========================================")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        menu_dict["starters"][1]["Spring Rolls"]["Quantity"] += 1
    elif choice == 2:
        menu_dict["starters"][2]["French Onion Soup"]["Quantity"] += 1
    elif choice == 3:
        menu_dict["starters"][3]["Tomato Bruschetta"]["Quantity"] += 1
    elif choice == 4:
        menu_dict["starters"][4]["Caesar Salad"]["Quantity"] += 1
    elif choice == 0:
        menu()
    starters()


def main_course():
    print("=================MAIN COURSE=================")
    print("1. Grilled Salmon with Dilled Sauce")
    print("2. Roast Beef with Vegetables")
    print("3. Chicken and Mushroom Pie")
    print("4. MarraKesh Vegetarian Curry")
    print("5. Eggplant Lasagne")
    print("0. Go back to Main Menu")
    print("=============================================")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        menu_dict["main_course"][1]["Grilled Salmon with Dilled Sauce"]["Quantity"] += 1
    elif choice == 2:
        menu_dict["main_course"][2]["Roast Beef with Vegetables"]["Quantity"] += 1
    elif choice == 3:
        menu_dict["main_course"][3]["Chicken and Mushroom Pie"]["Quantity"] += 1
    elif choice == 4:
        menu_dict["main_course"][4]["MarraKesh Vegetarian Curry"]["Quantity"] += 1
    elif choice == 5:
        menu_dict["main_course"][5]["Eggplant Lasagne"]["Quantity"] += 1
    elif choice == 0:
        menu()
    main_course()


def desserts():
    print("=============DESSERTS=============")
    print("1. Apple Pie with Cream")
    print("2. Lemon Meringue Pie")
    print("3. Vanilla Ice Cream")
    print("4. Crêpe Suzette")
    print("5. Fruit Salad")
    print("0. Go back to Main Menu")
    print("==================================")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        menu_dict["desserts"][1]["Apple Pie with Cream"]["Quantity"] += 1
    elif choice == 2:
        menu_dict["desserts"][2]["Lemon Meringue Pie"]["Quantity"] += 1
    elif choice == 3:
        menu_dict["desserts"][3]["Vanilla Ice Cream"]["Quantity"] += 1
    elif choice == 4:
        menu_dict["desserts"][4]["Crêpe Suzette"]["Quantity"] += 1
    elif choice == 5:
        menu_dict["desserts"][5]["Fruit Salad"]["Quantity"] += 1
    elif choice == 0:
        menu()
    desserts()


def bill_extract(food_type):
    global amount
    for i in range(1, len(menu_dict[food_type]) + 1):
        # food_name = str(menu_dict["starters"][i])
        temp = str(menu_dict[food_type].get(i))
        food_name = ""
        count = 0
        for j in range(1, len(temp)):
            if temp[j] == ":":
                break
            else:
                count += 1
        for k in range(2, count):
            food_name += temp[k]
        qty = int(menu_dict[food_type][i][food_name]["Quantity"])
        price = float(menu_dict[food_type][i][food_name]["Price"])
        if qty != 0:
            print(food_name, "| Quantity:", qty, "| Amount:", (price * qty))
            amount += price


def bill_print():
    print("===================================BILL=====================================")
    print("=                                                                          =")
    print("=================================STARTERS===================================")
    """global amount
    for i in range(1, len(menu_dict["starters"]) + 1):
        # food_name = str(menu_dict["starters"][i])
        temp = str(menu_dict["starters"].get(i))
        food_name = ""
        count = 0
        for j in range(1, len(temp)):
            if temp[j] == ":":
                break
            else:
                count += 1
        for k in range(2, count):
            food_name += temp[k]
        qty = int(menu_dict["starters"][i][food_name]["Quantity"])
        price = float(menu_dict["starters"][i][food_name]["Price"])
        if qty != 0:
            print(food_name, "| Quantity:", qty, "| Amount:", (price * qty))
            amount += price
            # print(food_name, "| Quantity:", qty)"""
    bill_extract("starters")
    print("===============================MAIN COURSE==================================")
    """for i in range(1, len(menu_dict["main_course"]) + 1):
        temp = str(menu_dict["main_course"][i])
        food_name = ""
        count = 0
        for j in range(1, len(temp)):
            if temp[j] == ":":
                break
            else:
                count += 1
        for k in range(2, count):
            food_name += temp[k]
        qty = int(menu_dict["main_course"][i][food_name]["Quantity"])
        price = float(menu_dict["main_course"][i][food_name].get("Price"))
        if qty != 0:
            print(food_name, "| Quantity:", qty, "| Amount:", (price * qty))
            amount += price
            # print(food_name, "| Quantity:", qty)"""
    bill_extract("main_course")
    print("================================DESSERTS====================================")
    """for i in range(1, len(menu_dict["desserts"]) + 1):
        temp = str(menu_dict["desserts"][i])
        food_name = ""
        count = 0
        for j in range(1, len(temp)):
            if temp[j] == ":":
                break
            else:
                count += 1
        for k in range(2, count):
            food_name += temp[k]
        qty = int(menu_dict["desserts"][i][food_name]["Quantity"])
        price = float(menu_dict["desserts"][i][food_name]["Price"])
        if qty != 0:
            print(food_name, "| Quantity:", qty, "| Amount:", (price * qty))
            amount += price
            # print(food_name, "| Quantity:", qty)"""
    bill_extract("desserts")
    print("============================================================================")
    print("Total amount =", amount)
    print("============================================================================")
    exit()


menu()
