# TODO

time1 = input("Please enter the first time: ")
time2 = input("Please enter the second time: ")
final_time = str(int(time2) - int(time1))
if str(time1[0]) == "0":
    print (final_time[0],"hours", final_time[1:], "minutes")
else:
    print (final_time[:2],"hours", final_time[2:], "minutes")
