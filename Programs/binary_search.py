from timeit import default_timer as timer
import math

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input = 8

start = timer()
while True:
    element = list1[len(list1)//2]
    if input > element:
        list1 = list1[len(list1)//2:len(list1) - 1]
    elif input < element:
        list1 = list1[0:len(list1)//2]
    elif input == element:
        print("Element found!")
        print("Position=", len(list1)//2)
        break
    else:
        print("Element not found!")
end = timer()

runtime = math.ceil((end - start)*1e6)/1000
print("Time taken:", runtime)