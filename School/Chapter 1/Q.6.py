def calculate(length_feet):
    length_inches = length_feet * 12
    return length_inches

def inputing():
    num = float(input("Enter the length in feet: "))
    return num

def outputing(final_value):
    print("The length in inches is", final_value)

num = inputing()
value = calculate(num)
outputing(value)
