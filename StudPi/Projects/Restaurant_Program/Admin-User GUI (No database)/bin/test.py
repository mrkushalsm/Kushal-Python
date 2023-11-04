menu_dict = {"starters": {1: {"Spring Rolls": {"Price": 100, "Quantity": 0}},
                          2: {"French Onion Soup": {"Price": 100, "Quantity": 0}},
                          3: {"Tomato Bruschetta": {"Price": 100, "Quantity": 0}},
                          5: {"Caesar Salad": {"Price": 100, "Quantity": 0}}},

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

food_type = "starters"

bbg = menu_dict[food_type].keys()
bbg = list(bbg)
bbg = bbg[len(bbg) - 1]
bbg = bbg + 1

print(bbg)
