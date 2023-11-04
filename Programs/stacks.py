stack = []

def stack():
    stack = []
    return stack

def empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

def size(stack):
    return len(stack)

def top(stack):
    return id(stack[len(stack) - 1])

def push(stack, element):
    stack.append(element)
    print("Pushed item:", element)

def pop(stack):
    if empty(stack):
        print("Stack is empty!")
    else:
        stack.pop()
