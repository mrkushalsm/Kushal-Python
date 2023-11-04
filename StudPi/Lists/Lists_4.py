name = ["Izabella", "Lawrence", "Brendan", "Duncan", "Trenton", "Ashlyn", "Marie", "Adriel", "Angela", "Eden",
        "Ashanti", "Royce"]
phone_no = [2832020875, 4049715228, 5237500615, 9330859600, 5669764359, 4112288133, 3552129240, 4171024511,
            1346261702, 1513718483]

name_input = input("Enter the name whose number you want: ")
for i in range(10):
    if name[i] == name_input:
        print(f"The name '{name_input}' found")
        print("Their number is", phone_no[i])
        exit()

print(f"The name '{name_input}' not found")