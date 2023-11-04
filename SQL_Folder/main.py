import mysql.connector as sql

mycon = sql.connect(host="localhost", user="root", passwd="Kushal25@MYSQL", database="menagerie")
cursor = mycon.cursor()
a= input("Enter one: ")
b= input("Enter two: ")
cursor.execute("select {} from {}".format(a, b))
event = cursor.fetchall()
print(event)
mycon.close()