from curses.ascii import isalpha
from datetime import date, datetime
import mysql.connector as sql

mycon = sql.connect(host="localhost", user="root", passwd="Kushal25@MYSQL")
cursor = mycon.cursor()

def create_tables():
    if mycon.is_connected:
        command = "create database if not exists Shri_Ram_Bank;"
        cursor.execute(command)
        command = "use Shri_Ram_bank;"
        cursor.execute(command)
        command = "create table if not exists Accounts(name varchar(30), username varchar(20), password tinytext, Date_of_birth date, address varchar(40), Mobile_Number varchar(30), Aadhar_no varchar(30), Balance int);"
        cursor.execute(command)
        command = "create table if not exists Transactions(credited int, debited int, username varchar(20), transaction_date date);"
        cursor.execute(command)
        main_page()
    else:
        print("There is problem connecting to the database, please try again later!")

def withdraw_money(username):
    try:
        command = "select Balance from Accounts where username='{}';".format(username)
        cursor.execute(command)
        bal = cursor.fetchone()[0]
    except Exception:
        print("Oops, we are having some technical issues at the moment. Please try again later!")
    print("\n")
    print("________________________________ ")
    print("Your Account Balance is : ", bal)
    print("_________________________________")
    print("\n")

    while True:
        try:
            amount = int(input("Enter the amount for withdrawl : "))
                                
        except ValueError:
            print("That was an invalid input. Try again!")
            print("\n")
            continue                           
                            
        if amount <= bal:
            credited = 0
                                
            command = "update Accounts set Balance=GREATEST(0,Balance - '{}') where username='{}';".format(amount, username)
            cursor.execute(command)
            mycon.commit()

            cursor.execute(command)
            mycon.commit()
            date_rn = date.today()
            command = "insert into Transactions values('{}','{}','{}','{}');".format(credited, amount, username, date_rn)
            cursor.execute(command)
            mycon.commit()

            command = "SET FOREIGN_KEY_CHECKS=1"
            cursor.execute(command)
            mycon.commit()

            command = "select Balance from Accounts where username='{}';".format(username)
            cursor.execute(command)
            balance=cursor.fetchone()[0]
            print("\n")
            print("____________________________________________________________________")
            print("Your username ", username, "is debited with Rs", amount ,"on " , date_rn)
            print("towards Net Banking. Available balance is Rs : " , balance, " ₹ only ")
            print("________________________________________________________________________")
            break
            
        elif amount > bal:
            print("Insufficient Balance. Please Try Again!")
            continue

def deposit_money(username):
    debited=0                            
    while True:
        try:   
            amount=(input("Enter the amount to deposit : "))
            if amount.isalpha():
                raise TypeError
            else:
                                                            
                command = "update Accounts set Balance=Balance +'{}' where username='{}';".format(amount,username)
                cursor.execute(command)
                mycon.commit()
                date_rn = date.today()
                command = "insert into Transactions values('{}','{}','{}','{}');".format(amount, debited, username, date_rn)
                cursor.execute(command)
                mycon.commit()
                command = "select Balance from Accounts where username='{}';".format(username)
                cursor.execute(command)
                balance = cursor.fetchone()[0]
                print("\n")
                print("____________________________________________________________________")
                print("Your username ", username, "is Credited with Rs", amount, "on ", date_rn)
                print("towards Net Banking. Available balance is Rs : " , balance, " ₹ only")
                print("________________________________________________________________________")
                break
        except TypeError:
            print("Please enter a number. Try again!")
            continue

def last_transactions(username):
    command = "select credited, debited, username, transaction_date from Transactions where username='{}';".format(username)
    cursor.execute(command)
    print("_______________________________________________________________________________")
    print("***************** The Transaction Details are as Follows **********************")
    print("\n")
    for i in cursor.fetchall():
        print("___________________________________________________________________________")
        print("Credited , Debited  : " ,i)
        print("___________________________________________________________________________")

def view_profile(username):
    command = "Select name, username, Password,  address,  Mobile_Number, Aadhar_no, Balance from Accounts where username='{}';".format(username)
    cursor.execute(command)
    print("______________________________________________________________________________")
    print("****************************** Account Details *******************************")
    print("______________________________________________________________________________")
    print("\n")
    print("_______________________________________________________________________________")
    print("    Name      User Name  PassWord   Address     Mob No \t   Aadhar No    Balance")
    print("_______________________________________________________________________________")
    print("\n")
    for i in cursor.fetchall():
        print("______________________________________________________________________________")
        print(i)
        print("______________________________________________________________________________")

def update_acc_details(username):
    while True:
        print("\n")
        print("______________________________________________________")
        print("****************** Account Setting *******************")
        print("______________________________________________________")
                        
        print("Enter 1 To Update Your Name : ")
        print("Enter 2 To Update Your Username : ")                        
        print("Enter 3 To Update Your Password : ")
        print("Enter 4 To Update Your Phone Number : ")
        print("Enter 5 To Update Address : ")
        print("Enter 0 to Go Back")
        print("______________________________________________________")
                        
        try:
            choice = int(input("Enter Your Choice : "))
            if choice > 5 or choice < -1:
                raise ValueError
            elif choice == 1:
                new_name = input("Enter your new name: ")
                command = "update Accounts set name='{}' where username='{}';".format(new_name, username)
                cursor.execute(command)
                mycon.commit()
                print("Name has been updated successfully!")
            elif choice == 2:
                new_username = input("Enter your new username: ")
                command = "update Accounts set username='{}' where username='{}';".format(new_username, username)
                cursor.execute(command)
                mycon.commit()
                print("Username has been updated successfully!")
                username =  new_username
            elif choice == 3:
                new_password = input("Enter your new password: ")
                command = "update Accounts set password='{}' where username='{}';".format(new_password, username)
                mycon.commit()
                print("Password has been updated successfully!")
            elif choice == 4:
                new_phone_no = int(input("Enter your new phone number: "))
                command = "update Accounts set Mobile_Number='{}' where username='{}';".format(new_phone_no, username)
                mycon.commit()
                print("Phone number has been updated successfully!")
            elif choice == 5:
                new_address = input("Enter your new address: ")
                command = "update Accounts set address='{}' where username='{}';".format(new_address, username)
                mycon.commit()
                print("Addresss has been updated successfully!")
            elif choice == 0:
                logged_in_page()
                                    
        except ValueError:
            print("That was not a valid number. Try again!")
            continue

def delete_acc(username):
    
    cursor.execute(command)
    mycon.commit()
    command = "delete from Accounts where username='{}';".format(username)
    cursor.execute(command)
    mycon.commit()

    command = "delete from Transactions where username='{}';".format(username)
    cursor.execute(command)
    mycon.commit()
                    
    command = "SET FOREIGN_KEY_CHECKS=1"
    cursor.execute(command)
    mycon.commit()

    print("Your account has been deleted successfully!")

def logged_in_page(username, password):
    print("\n")
    print("_________________________________________________________________")
    print("******************* Welcome To Shri Ram Bank  *******************")
    print("_________________________________________________________________")
    print("\n")
    print("Enter 1 to Withdraw Money")
    print("Enter 2 to Deposit Money")
    print("Enter 3 to View Last Five Transaction ")
    print("Enter 4 to View Your Profile ")
    print("Enter 5 to Update Account Deatils")
    print("Enter 6 to Delete Your Account Permanently : ")
    print("Enter 7 for Log Out")
    print("_________________________________________________________________")

    try:

        choice = int(input("Enter Your Choice : "))
        if choice > 7 or choice < 1:
            raise Exception
        elif choice == 1:
            withdraw_money(username)
        elif choice == 2:
            deposit_money(username)
        elif choice == 3:
            last_transactions(username)
        elif choice == 4:
            view_profile(username)
        elif choice == 5:
            update_acc_details(username, password)
        elif choice == 6:
            delete_acc(username)
        elif choice == 7:
            print("Logged out")
            print("Thank you for choosing Shri Ram Bank!")
            main_page()
    except Exception:
        print("That was not a valid number. Try again!")
        logged_in_page()

def sign_up():
    specialsyms = ['$', '@', '#', '%']

    while True:
        try: 
            sch1 = '.'
            sch2 = '#'
            sch3 = '$'
            sch4 = '*'
            sch5 = '&'
            sch6 = '='
            sch7 = ','
            sch8 = '@'
            sch9 = '?'
            sch10 = '/'
            name = input("Enter Your Name Here : ")
            if (name in sch1) or (name in sch2) or (name in sch3) or (name in sch4) or (name in sch5) or (name in sch6) or (name in sch7) or (name in sch8) or (name in sch9) or (name in sch10):
                raise TypeError 
            break
        except TypeError:
            print("Special Character are not allowed like . , @ # < > ? / ; ")
            continue

    while True:
        try:
            ch1 = '.'
            ch2 = ','
            ch3 = '@'
            ch4 = '#'
            ch5 = '$'
            ch6 = '%'
            ch7 = '*'
            ch8 = '&'
            ch9 = '='
            ch10 = '<'
            ch11 = '>'
            ch12 = '?'
            ch13 = "!"
            username = input("Enter Your User Name : ")
            if(ch1 in username) or (ch2 in username) or (ch3 in username) or (ch4 in username) or (ch5 in username) or (ch6 in username) or (ch7 in username) or (ch8 in username) or (ch9 in username) or (ch10 in username) or (ch11 in username) or (ch12 in username) or (ch13 in username):
                raise TypeError 
            break
        except TypeError:
            print("Special Character are not allowed like . ,@ # $ % * & = < > ? !")
            continue
    
    while True:        
        try:
            password = input("Enter Your Password : ")
            if (len(password) < 6):
                raise ValueError ("Password should contain at least 6 character")
            if not any(char.isdigit() for char in password):
                raise ValueError ("Password should atleast a number")
            if not any(char.isupper() for char in password):
                raise KeyError ()
            if not any(char.islower() for char in password):
                raise KeyError
            if not any(char in specialsyms for char in password):
                raise KeyError
            break
        except ValueError:
            print("Password should contain atleast 1 upper case, 1 Lower Case , 1 Special Character  and Password Must Contain atleast 7 character")
            continue
        except KeyError:
            print("Password should contain atleast 1 upper case, 1 Lower Case , 1 Special Character  and Password Must Contain atleast 7 character")
            continue
    
    amount = int(input("Enter the Amount of money you want to deposit : "))
    
    while True:
        try:
            date_input = input("Enter Your Date of Birth : ")
            birth = datetime.strptime(date_input, "%d/%m/%Y")
            birth =  birth.date()
            break
        except ValueError:
            print("Please enter Date of birth in proper format !!! DD/MM/YYYY")
            continue
    
    address = input("Enter Your Address : ")

    while True:
        try:
            phone_no = input("Enter Your Phone Number : ")
            if (len(phone_no) != 10) or (phone_no.isalpha()):
                raise ValueError("Pls enter a valid 10 digit Number")
            break
        except ValueError as error:
            print(error)
            continue
    
    while True:
        try:
            aadhar_no=input("Enter Your 12 Digit Aadhar Number : ")
            if(len(aadhar_no) != 12) or (aadhar_no.isalpha()):
                raise ValueError ("Please Enter a valid 12 digit aadhar Number")
            break
        except ValueError as error:
            print(error)
            continue
    
    query = "insert into Accounts values('{}','{}','{}','{}','{}','{}','{}','{}');".format(name, username, password, birth, address, phone_no, aadhar_no, amount)
    cursor.execute(query)
    mycon.commit()
    print("\n")
    print("_________________________________________________________________________")
    print("********** Account Has Been Created Successfully Kindly Login ***********")
    print("_________________________________________________________________________")

def sign_in():
    print("(Enter 0 to exit)")
    username = input("Enter Your Username : ")
    if username != 0:
        password = input("Enter Your Password : ")
        if password != 0:
            command = "select * from Accounts where username='{}' and password='{}';".format(username, password)
            cursor.execute(command)
            data = cursor.fetchall()
            if data:
                logged_in_page(username, password)
            else:
                print("Invalid username or password!")
        else:
            main_page()
    else:
        main_page()
    

def main_page():
    print("\n")
    print("_________________________________________________________________")
    print("******************* Welcome To Shri Ram Bank  *******************")
    print("_________________________________________________________________")
    print("Enter 1 to for Sign Up ")
    print("Enter 2 to for Sign In  ")
    print("Enter 0 to exit")
    print("_________________________________________________________________")
    
    try:
        choice = int(input("Enter your choice: "))
        if choice > 2 or choice < -1:
            print("That was not a valid number. Try again!")
            main_page()
        elif isalpha(choice):
            raise Exception
        else:
            if choice == 1:
                sign_up()
            elif choice == 2:
                sign_in()
            elif choice == 0:
                print("Thank you for using our program!")
                exit()
    except Exception:
        print("You must enter a number. Try again!")
        main_page()

create_tables()