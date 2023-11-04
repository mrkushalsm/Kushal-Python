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


def display_menu_label_func(food_type):
    bill_format = ""
    for i in range(1, (len(menu_dict[food_type]) + 1)):
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

    print(bill_format)


display_menu_label_func("starters")
