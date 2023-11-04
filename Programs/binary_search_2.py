from timeit import default_timer as timer
import math

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input = 8

start = timer()
while True:
    position = len(list1)//2
    element = list1[position]
    if input > element:
        list1 = list1[position:len(list1) - 1]
    elif input < element:
        list1 = list1[0:position]
    elif input == element:
        print("Element found!")
        print("Position=", position)
        break
    else:
        print("Element not found!")
end = timer()

runtime = math.ceil((end - start)*1e6)/1000
print("Time taken:", runtime)