import math

print("Enter the first time (in hours, minutes and seconds): ")
hour_1 = float(input())
minute_1 = float(input())
seconds_1 = float(input())

print("Enter the second time (in hours, minutes and seconds): ")
hour_2 = float(input())
minute_2 = float(input())
seconds_2 = float(input())

total_time_seconds_1 = (hour_1 * 3600) + (minute_1 * 60) + seconds_1
total_time_seconds_2 = (hour_2 * 3600) + (minute_2 * 60) + seconds_2

difference = math.abs(total_time_seconds_1 - total_time_seconds_1)

total_hours = (difference % (24 * 3600)) / 3600
total_minutes = (difference % (24 * 3600 * 3600)) / 60
total_seconds = (difference % (24 * 3600 * 3600 * 60)) / 60

print("The difference of the two times are", total_hours, "hours,", total_minutes, "minutes and", total_seconds)