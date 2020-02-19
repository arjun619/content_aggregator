import getpass
import login
import urllib.request
import data_management as db
def getlogindetails():
    name=input("enter the full user name ")
    dname=input("enter the display name ")
    password=getpass.getpass()
    user_created=login.user_data(name,dname,password)
    return user_created

def menu():
    print("\nWhat would you try to know about we have got \n")
    print("\n1. Data Science\n")
    print("\n2. Sports News\n")
    print("\n3. Press 0 to exit\n")
def link_display(content):
    for i in range(len(content)):
        print(i,content[i][0],end="\n\n")
    k=int(input("Select the option you wanna see\n\n"))
    print(content[k][1])

def connect():
    name=input("Enter full name\n")
    dname=input("Enter display name\n")
    password=getpass.getpass()
    user_created=login.user_data(name,dname,password)
    return user_created


    
def check_new_user():
    flag=input("\n\nAre you a new user\n\n")
    if (flag[0]=="Y" or flag[0]=="y"):
        user_data=getlogindetails()
        db.insert_into_database(user_data)
    elif (flag[0]=="N" or flag[0]=="n"):
        connect()

