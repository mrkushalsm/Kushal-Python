def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def switch_case(choice, a, b):
    if choice == 1 :
        print(a, "+", b, "=", add(a, b))
    elif choice == 2 :
        print(a, "-", b, "=", sub(a, b))
    elif choice == 3 :
        print(a, "x", b, "=", mult(a, b))
    elif choice == 4 :
        print(a, "/", b, "=", div(a, b))
    elif choice == 5 :
        exit()

def display():
    print("==MAIN MENU==")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("=============")
    choice = int(input("Enter your choice: "))
    print("Enter two numbers: ")
    a = float(input())
    b = float(input())
    switch_case(choice, a, b)

display()