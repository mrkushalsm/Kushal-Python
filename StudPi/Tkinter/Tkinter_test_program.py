import tkinter as tk
from functools import partial


def sum2(label):
    num3 = int(num1.get())  # extract value from num1 entry field
    num4 = int(num2.get())  # extract value from b entry field
    sum1 = num3 + num4
    sum_label = tk.Label(root, text=sum1).grid(row=4, column=2)
    label.config(bg="red", text='now red')


root = tk.Tk()  # instance of Tkinter basically a screen
num1 = tk.StringVar()
num2 = tk.StringVar()

# num1 = tk.StringVar()
# b = tk.StringVar()

# add first label and an entry field in the screen
label1 = tk.Label(root, text='Enter 1st number ', bg="red").grid(row=1, column=1)  # place the lable in row 1 cloumn
# 1 with text as enter first number
entry1 = tk.Entry(root, textvariable=num1).grid(row=1, column=2)  # place the input field in row 2 column 1 with no text

# add second label and an entry field in the screen
label2 = tk.Label(root, text='Enter 2nd number ').grid(row=2, column=1)
entry2 = tk.Entry(root, textvariable=num2).grid(row=2, column=2)

# adding a button and adding sum function on click of the same
label3 = tk.Label(root, text="initially green", fg="green")
label3.grid(row=4, column=1)
sum2 = partial(sum2, label3)
buttonCal = tk.Button(root, text="Add", command=partial(sum2)).grid(row=3, column=1)

root.mainloop()
