date = input("Enter the date (MMDDYYYY): ")
if date[:2] == "01":
    month = "January"
elif date[:2] == "02":
    month = "Febuary"
elif date[:2] == "03":
    month = "March"
elif date[:2] == "04":
    month = "April"
elif date[:2] == "05":
    month = "May"
elif date[:2] == "06":
    month = "June"
elif date[:2] == "07":
    month = "July"
elif date[:2] == "08":
    month = "August"
elif date[:2] == "09":
    month = "September"
elif date[:2] == "10":
    month = "October"
elif date[:2] == "11":
    month = "November"
elif date[:2] == "12":
    month = "December"

if date[2] == "0":
    day = date[3]
else:
    day = date[2:4]

year = date[4:]

print(month, day + ",", year)
