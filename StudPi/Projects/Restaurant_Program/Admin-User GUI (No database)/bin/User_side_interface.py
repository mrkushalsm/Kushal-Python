import tkinter as tk
from PIL import ImageTk, Image
import os

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

this_dir = os.path.dirname(__file__)

amount = 0


def main_menu():
    main_menu_window = tk.Tk()
    main_menu_window.title("Restaurant Menu (User interface)")
    main_menu_window.iconphoto(False, tk.PhotoImage(file=os.path.join(this_dir, "..", "images", "icon", "icon.png")))

    main_menu_frame = tk.LabelFrame(main_menu_window)
    main_menu_frame.pack(padx=5, pady=5)

    starters_button = tk.Button(main_menu_frame, text="Starters", height=10, width=30,
                                command=lambda: starters(main_menu_window))
    main_course_button = tk.Button(main_menu_frame, text="Main Course", height=10, width=30,
                                   command=lambda: main_course(main_menu_window))
    desserts_button = tk.Button(main_menu_frame, text="Desserts", height=10, width=30,
                                command=lambda: desserts(main_menu_window))
    print_bill_button = tk.Button(main_menu_frame, text="Print the bill", height=10, width=30,
                                  command=lambda: bill_display(main_menu_window))

    starters_button.grid(row=1, column=1)
    main_course_button.grid(row=1, column=2)
    desserts_button.grid(row=2, column=1)
    print_bill_button.grid(row=2, column=2)

    main_menu_window.mainloop()


def starters(main_menu_window):
    main_menu_window.destroy()
    starters_window = tk.Tk()
    starters_window.title("Restaurant Menu (User interface)")
    starters_window.iconphoto(False, tk.PhotoImage(file=os.path.join(this_dir, "..", "images", "icon", "icon.png")))

    starters_frame = tk.LabelFrame(starters_window)
    starters_frame.grid(row=1, column=1, padx=5, pady=5)

    """CODE"""

    display_food(starters_frame, "starters", "Spring Rolls.jpg", 170, 100, 1, 1, "Spring Rolls", 1)
    display_food(starters_frame, "starters", "French Onion Soup.jpeg", 170, 100, 2, 1, "French Onion Soup", 2)
    display_food(starters_frame, "starters", "Tomato Bruschetta.jpeg", 170, 100, 3, 1, "Tomato Bruschetta", 3)
    display_food(starters_frame, "starters", "Caesar Salad.jpeg", 170, 100, 4, 1, "Caesar Salad", 4)

    back_button = tk.Button(starters_frame, text="Go back to main menu",
                            command=lambda: back_to_menu(starters_window))
    back_button.grid(row=5, column=3, pady=20)

    starters_window.mainloop()


def main_course(main_menu_window):
    main_menu_window.destroy()
    main_course_window = tk.Tk()
    main_course_window.title("Restaurant Menu (User interface)")
    main_course_window.iconphoto(False, tk.PhotoImage(file=os.path.join(this_dir, "..", "images", "icon", "icon.png")))

    main_course_frame = tk.LabelFrame(main_course_window)
    main_course_frame.grid(row=1, column=1, padx=5, pady=5)

    """CODE"""

    display_food(main_course_frame, "main_course", "Grilled Salmon with Dilled Sauce.jpeg", 170, 100, 1, 1,
                 "Grilled Salmon with Dilled Sauce", 1)
    display_food(main_course_frame, "main_course", "Roast Beef with Vegetables.jpeg", 170, 100, 2, 1,
                 "Roast Beef with Vegetables", 2)
    display_food(main_course_frame, "main_course", "Chicken and Mushroom Pie.jpeg", 170, 100, 3, 1,
                 "Chicken and Mushroom Pie", 3)
    display_food(main_course_frame, "main_course", "MarraKesh Vegetarian Curry.jpeg", 170, 100, 4, 1,
                 "MarraKesh Vegetarian Curry", 4)
    display_food(main_course_frame, "main_course", "Eggplant Lasagne.jpeg", 170, 100, 5, 1, "Eggplant Lasagne", 5)

    back_button = tk.Button(main_course_frame, text="Go back to main menu",
                            command=lambda: back_to_menu(main_course_window))

    back_button.grid(row=6, column=3, pady=20)

    main_course_window.mainloop()


def desserts(main_menu_window):
    main_menu_window.destroy()
    desserts_window = tk.Tk()
    desserts_window.title("Restaurant Menu (User interface)")
    desserts_window.iconphoto(False, tk.PhotoImage(file=os.path.join(this_dir, "..", "images", "icon", "icon.png")))

    desserts_frame = tk.LabelFrame(desserts_window)
    desserts_frame.grid(row=1, column=1, padx=5, pady=5)

    """CODE"""

    display_food(desserts_frame, "desserts", "Apple Pie with Cream.jpeg", 170, 100, 1, 1, "Apple Pie with Cream", 1)
    display_food(desserts_frame, "desserts", "Lemon Meringue Pie.jpeg", 170, 100, 2, 1, "Lemon Meringue Pie", 2)
    display_food(desserts_frame, "desserts", "Vanilla Ice Cream.jpeg", 170, 100, 3, 1, "Vanilla Ice Cream", 3)
    display_food(desserts_frame, "desserts", "Crêpe Suzette.jpeg", 170, 100, 4, 1, "Crêpe Suzette", 4)
    display_food(desserts_frame, "desserts", "Fruit Salad.jpeg", 170, 100, 5, 1, "Fruit Salad", 5)

    back_button = tk.Button(desserts_frame, text="Go back to main menu",
                            command=lambda: back_to_menu(desserts_window))

    back_button.grid(row=6, column=3, pady=20)

    desserts_window.mainloop()


def back_to_menu(window):
    window.destroy()
    main_menu()


def display_food(frame, group, img_name, width, height, row, column, food_name, special_dict_id):
    food_name_label = tk.Label(frame, text=food_name)
    food_name_label.grid(row=row, column=column, padx=10)

    img = Image.open(os.path.join(this_dir, "..", "images", "food", group, img_name))
    img = img.resize((width, height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(frame, image=img)
    img_label.photo = img
    img_label.grid(row=row, column=(column + 1))

    price = str(menu_dict[group][special_dict_id][food_name]["Price"])
    price_label = tk.Label(frame, text="Price: " + price)
    price_label.grid(row=row, column=(column + 2), padx=20)

    count_label = tk.Label(frame, text="0")
    count_label.grid(row=row, column=(column + 4), padx=20)

    count_display(frame, group, row, column, food_name, special_dict_id)


def count_increase(frame, group, row, column, food_name, special_dict_id):
    menu_dict[group][special_dict_id][food_name]["Quantity"] += 1
    count_display(frame, group, row, column, food_name, special_dict_id)


def count_decrease(frame, group, row, column, food_name, special_dict_id):
    menu_dict[group][special_dict_id][food_name]["Quantity"] -= 1
    count_display(frame, group, row, column, food_name, special_dict_id)


def count_display(frame, group, row, column, food_name, special_dict_id):
    if menu_dict[group][special_dict_id][food_name]["Quantity"] > 9:
        count_label = tk.Label(frame, text="" + str(menu_dict[group][special_dict_id][food_name]["Quantity"]))
    else:
        count_label = tk.Label(frame, text="0" + str(menu_dict[group][special_dict_id][food_name]["Quantity"]))
    count_label.grid(row=row, column=(column + 4), padx=20)
    plus_button = tk.Button(frame, text="+", height=1, width=3, command=lambda: count_increase(frame, group, row,
                                                                                               column, food_name,
                                                                                               special_dict_id))
    plus_button.grid(row=row, column=(column + 3), padx=20)

    if menu_dict[group][special_dict_id][food_name]["Quantity"] <= 0:
        minus_button = tk.Button(frame, text="-", height=1, width=3, state=tk.DISABLED)
    else:
        minus_button = tk.Button(frame, text="-", height=1, width=3, command=lambda: count_decrease(frame, group, row,
                                                                                                    column, food_name,
                                                                                                    special_dict_id))
    minus_button.grid(row=row, column=(column + 5), padx=20)


def bill_display(main_menu_window):
    main_menu_window.destroy()
    bill_display_window = tk.Tk()
    bill_display_window.title("Restaurant Menu (User interface)")
    bill_display_window.iconphoto(False, tk.PhotoImage(file=os.path.join(this_dir, "..", "images", "icon", "icon.png")))

    bill_display_frame_1 = tk.LabelFrame(bill_display_window)
    bill_display_frame_1.grid(row=1, column=1, padx=5, pady=5)

    bill_display_frame_2 = tk.LabelFrame(bill_display_frame_1)
    bill_display_frame_2.grid(row=1, column=1, padx=5, pady=5)

    global amount

    """CODE"""

    string = ""
    string += "===================================BILL=====================================\n"
    string += "=\t\t\t\t\t\t\t\t\t                                       =\n"
    string += "=================================STARTERS===================================\n\n"
    string += bill_extract("starters") + "\n"
    string += "===============================MAIN COURSE==================================\n\n"
    string += bill_extract("main_course") + "\n"
    string += "================================DESSERTS====================================\n\n"
    string += bill_extract("desserts") + "\n"
    string += "============================================================================\n"
    string += "Total amount = " + str(amount) + "\n"
    string += "============================================================================\n"

    print_bill_button = tk.Button(bill_display_frame_1, text="Print the bill to a text file",
                                  command=lambda: print_bill_txt(string, bill_display_window))
    back_button = tk.Button(bill_display_frame_1, text="Go back to main menu",
                            command=lambda: back_to_menu(bill_display_window))

    bill_display_label = tk.Label(bill_display_frame_2, text=string)
    bill_display_label.pack()

    print_bill_button.grid(row=2, column=1, pady=10)
    back_button.grid(row=3, column=1, pady=10)

    bill_display_window.mainloop()


def bill_extract(food_type):
    global amount
    bill_format = ""
    for i in range(1, len(menu_dict[food_type]) + 1):
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
        if qty != 0:
            price = qty * float(menu_dict[food_type][i][food_name]["Price"])
            bill_format += food_name + " | Quantity: " + str(qty) + " | Amount: " + str(price * qty) + "\n"
            amount += price
    return bill_format


def print_bill_txt(string, window):
    bill = open("bill.txt", "w+")
    bill.write(string)
    bill.close()

    end_program(window)


def end_program(window):
    window.destroy()
    goodbye_window = tk.Tk()
    goodbye_window.title("Restaurant program (User interface)")
    goodbye_window.iconphoto(False, tk.PhotoImage(file=os.path.join(this_dir, "..", "images", "icon", "icon.png")))

    goodbye_label = tk.Label(text="Thank you for using our program", padx=20, pady=20)
    goodbye_label.pack()

    window.after(5000, goodbye_window.destroy)

    goodbye_window.mainloop()


if __name__ == '__main__':
    main_menu()
