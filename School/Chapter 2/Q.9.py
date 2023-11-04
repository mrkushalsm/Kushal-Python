month_days = {"January": 31, "Febuary": 28, "March": 31, "April": 30, "May": 31, "June": 30,
                "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, 
                "December": 31}

month = input("Enter a month: ")
print(month, "has", month_days[month], "days!")
print("Alphabetical order:", sorted(month_days))
for month_name in month_days:
    if month_days[month_name] == 31:
        print(month_name)
