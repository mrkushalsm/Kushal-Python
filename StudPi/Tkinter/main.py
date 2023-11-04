import tkinter as tk

root = tk.Tk()
root.title("Main")

# Creating a Label Widget
myLabel1 = tk.Label(root, text="Hello world")
myLabel2 = tk.Label(root, text="Welcome to my first Tkinter Program")

# Using the pack system to display label on the screen
# myLabel.pack()

# Using the grid system to display label on the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# Since Python is OOP, you can write the code like this too:-
# myLabel1 = tk.Label(root, text="Hello world").grid(row=0, column=0)


# Creating a function to be executed when a button is clicked
def button1_clicked():
    myLabel3 = tk.Label(root, text="Button working")
    myLabel3.grid(row=5, column=0)


# Creating and input field and a button command
myInputField3 = tk.Entry(width=50)


def button3_clicked():
    myLabel4 = tk.Label(root, text=myInputField3.get())
    myLabel4.grid(row=9, column=0)


# Creating a Button Widget
myButton1 = tk.Button(root, text="Click me", command=button1_clicked)
myButton2 = tk.Button(root, text="Can't click on me", state=tk.DISABLED)
myButton3 = tk.Button(root, text="Size", padx=100, pady=100, bg="green", fg="blue", command=button3_clicked)

# Using the grid system to display label on screen
myButton1.grid(row=2, column=0)
myButton2.grid(row=3, column=0)
myButton3.grid(row=4, column=0)

# Creating an Input Field
myInputField1 = tk.Entry(width=50, bg="magenta", fg="black")
myInputField2 = tk.Entry(width=100, bg="gray", fg="black", borderwidth="10")

# Using the grid system to display the input field on screen
myInputField1.grid(row=6, column=0)
myInputField2.grid(row=7, column=0)
myInputField3.grid(row=8, column=0)

# Create main loop for the screen to add the elements and track the motion of the mouse and the clicks, etc
root.mainloop()
