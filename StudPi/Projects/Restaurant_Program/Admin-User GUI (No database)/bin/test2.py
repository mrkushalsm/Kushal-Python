import tkinter as tk

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

menu_dict_backup = {"starters": {1: {"Spring Rolls": {"Price": 100, "Quantity": 0}},
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


def main_menu():
    main_window = tk.Tk()
    main_window.title("Restaurant program (Admin interface)")

    main_window_frame = tk.LabelFrame(main_window)
    main_window_frame.grid(row=1, column=1, padx=5, pady=5)

    add_new_item_button = tk.Button(main_window_frame, text="Add new item to Menu", height=10, width=30,
                                    command=lambda: add_new_item(main_window))
    edit_item_button = tk.Button(main_window_frame, text="Edit Menu contents", height=10, width=30)
    delete_menu_item_button = tk.Button(main_window_frame, text="Delete item in Menu", height=10, width=30,
                                        command=lambda: delete_menu_item(main_window))
    save_menu_button = tk.Button(main_window_frame, text="Save new menu", height=10, width=30,
                                 command=lambda: print(menu_dict))

    add_new_item_button.grid(row=1, column=1)
    edit_item_button.grid(row=1, column=2)
    delete_menu_item_button.grid(row=2, column=1)
    save_menu_button.grid(row=2, column=2)

    main_window.mainloop()


def add_new_item(main_window):
    main_window.destroy()
    add_new_item_window = tk.Tk()
    add_new_item_window.title("Restaurant program (Admin interface)")
    add_new_item_frame = tk.LabelFrame(add_new_item_window)
    add_new_item_frame.grid(row=1, column=1, padx=5, pady=5)

    starters_button = tk.Button(add_new_item_frame, text="Starters", height=10, width=30,
                                command=lambda: add_new_item_input(add_new_item_window, "starters"))
    main_course_button = tk.Button(add_new_item_frame, text="Main Course", height=10, width=30,
                                   command=lambda: add_new_item_input(add_new_item_window, "main_course"))
    desserts_button = tk.Button(add_new_item_frame, text="Desserts", height=10, width=30,
                                command=lambda: add_new_item_input(add_new_item_window, "desserts"))
    back_to_menu_button = tk.Button(add_new_item_frame, text="Back to the menu", height=10, width=30,
                                    command=lambda: back_to_menu(add_new_item_window))

    starters_button.grid(row=1, column=1)
    main_course_button.grid(row=1, column=2)
    desserts_button.grid(row=2, column=1)
    back_to_menu_button.grid(row=2, column=2)

    add_new_item_window.mainloop()


def add_new_item_input(main_window, food_type):
    main_window.destroy()
    add_new_item_window = tk.Tk()
    add_new_item_window.title("Restaurant program (Admin interface)")
    add_new_item_frame = tk.LabelFrame(add_new_item_window)
    add_new_item_frame.grid(row=1, column=1, padx=5, pady=5)

    food_name_label = tk.Label(add_new_item_frame, text="Enter the food name: ", width=50)
    food_name_input = tk.Entry(add_new_item_frame, width=50)

    food_price_label = tk.Label(add_new_item_frame, text="Enter the food price: ", width=50)
    food_price_input = tk.Entry(add_new_item_frame, width=50)

    save_button = tk.Button(add_new_item_frame, text="Save to Menu",
                            command=lambda: add_new_item_save(add_new_item_window, food_type,
                                                              str(food_name_input.get()),
                                                              int(food_price_input.get()),
                                                              ((len(menu_dict[food_type].keys())) + 1)))

    back_to_menu_button = tk.Button(add_new_item_frame, text="Back to the menu",
                                    command=lambda: back_to_menu(add_new_item_window))

    food_name_label.grid(row=1, column=1, pady=10)
    food_name_input.grid(row=2, column=1)

    food_price_label.grid(row=3, column=1, pady=10)
    food_price_input.grid(row=4, column=1, pady=10)

    save_button.grid(row=5, column=1, pady=10)
    back_to_menu_button.grid(row=6, column=1, pady=10)

    add_new_item_window.mainloop()


def add_new_item_save(main_window, food_type, food_name, food_price, id_no):
    menu_dict[food_type].update(
        {id_no: {str(food_name): {"Price": food_price, "Quantity": 0}}})
    back_to_menu(main_window)


def delete_menu_item(main_window):
    main_window.destroy()
    delete_menu_item_window = tk.Tk()
    delete_menu_item_window.title("Restaurant program (Admin interface)")
    delete_menu_item_frame = tk.LabelFrame(delete_menu_item_window)
    delete_menu_item_frame.grid(row=1, column=1, padx=5, pady=5)

    starters_button = tk.Button(delete_menu_item_frame, text="Starters", height=10, width=30,
                                command=lambda: delete_menu_item_input(delete_menu_item_window, "starters"))
    main_course_button = tk.Button(delete_menu_item_frame, text="Main Course", height=10, width=30,
                                   command=lambda: delete_menu_item_input(delete_menu_item_window, "main_course"))
    desserts_button = tk.Button(delete_menu_item_frame, text="Desserts", height=10, width=30,
                                command=lambda: delete_menu_item_input(delete_menu_item_window, "desserts"))
    back_to_menu_button = tk.Button(delete_menu_item_frame, text="Back to the menu", height=10, width=30,
                                    command=lambda: back_to_menu(delete_menu_item_window))

    starters_button.grid(row=1, column=1)
    main_course_button.grid(row=1, column=2)
    desserts_button.grid(row=2, column=1)
    back_to_menu_button.grid(row=2, column=2)

    delete_menu_item_window.mainloop()


def delete_menu_item_input(main_window, food_type):
    main_window.destroy()
    delete_menu_item_input_window = tk.Tk()
    delete_menu_item_input_window.title("Restaurant program (Admin interface)")
    delete_menu_item_input_frame_1 = tk.LabelFrame(delete_menu_item_input_window)
    delete_menu_item_input_frame_1.grid(row=1, column=1, padx=5, pady=5)
    delete_menu_item_input_frame_2 = tk.LabelFrame(delete_menu_item_input_frame_1)
    delete_menu_item_input_frame_2.grid(row=1, column=1, padx=5, pady=5)

    food_id_label = tk.Label(delete_menu_item_input_frame_1, text="Enter the food id number: ", width=50)
    food_id_input = tk.Entry(delete_menu_item_input_frame_1, width=50)

    food_id_label.grid(row=2, column=1, pady=10)
    food_id_input.grid(row=3, column=1)

    delete_button = tk.Button(delete_menu_item_input_frame_1, text="Delete item from Menu",
                              command=lambda: delete_menu_item_delete(delete_menu_item_input_window, food_type,
                                                                      food_id_input.get()))

    back_to_menu_button = tk.Button(delete_menu_item_input_frame_1, text="Back to the menu",
                                    command=lambda: back_to_menu(delete_menu_item_input_window))

    delete_button.grid(row=5, column=1, pady=10)
    back_to_menu_button.grid(row=6, column=1, pady=10)

    delete_menu_item_input_window.mainloop()


def delete_menu_item_delete(main_window, food_type, food_id):
    length_food_type = int(len(menu_dict[food_type]))
    """if food_id == length_food_type:
        menu_dict[food_type].pop(food_id)
    elif food"""
    for i in range(int(food_id), length_food_type + 1):
        if i == length_food_type:
            menu_dict[food_type].pop(i)
            break
        elif i == int(food_id):
            menu_dict[food_type][i] = menu_dict[food_type][i + 1]
        elif i > int(food_id):
            menu_dict[food_type][length_food_type + 1] = menu_dict[food_type][i + 1]
            print(menu_dict)
            # menu_dict[food_type].pop(i + 1)
            # menu_dict[food_type].pop(i)
            print(menu_dict)
            menu_dict[food_type][i] = menu_dict[food_type][(length_food_type + 1)]
            print(menu_dict)
            menu_dict[food_type].pop(length_food_type + 1)
            print(menu_dict)
    # menu_dict[food_type].pop(len(menu_dict[food_type]))
    print(menu_dict)
    back_to_menu(main_window)


"""def display_menu_label_func(food_type):
    bill_format = ""
    food_id = 1
    increment = 1
    global deleted_food_id
    for i in range(1, (len(menu_dict[food_type]) + increment)):
        if deleted_food_id == i:
            increment += 1
            continue
        else:
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
            bill_format += str(food_id) + ". " + food_name + "\n"
            food_id += 1
    return bill_format"""


def back_to_menu(window):
    window.destroy()
    main_menu()


if __name__ == "__main__":
    print(len(menu_dict["desserts"]))
    main_menu()
