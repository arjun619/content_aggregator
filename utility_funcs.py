import getpass
import login
import urllib.request
import data_management as db
from random import randint
def getSignUpdetails():
    name=input("enter the full user name ")
    dname=input("enter the display name ")
    password=getpass.getpass()
    user_id=randint(1,1000000)
    user_created=login.user_data(name,dname,password,user_id)
    return user_created
def getLoginDetails():
    name=input("enter the full user name ")
    dname=input("enter the display name ")
    password=getpass.getpass()
    user_data=db.validate(name,dname,password)
    return user_data

def menu():
    print("\nWhat would you try to know about we have got \n")
    print("\n1. Data Science\n")
    print("\n2. Sports News\n")
    print("\n3. Press 0 to exit\n")
def link_display(user_data,content):
    for i in range(len(content)):
        print(i,content[i][0],end="\n\n")
    k=int(input("Select the option you wanna see\n\n"))
    print(content[k][1])
    db.history_store(user_data,content[k][1])


"""def connect():
    name=input("Enter full name\n")
    dname=input("Enter display name\n")
    password=getpass.getpass()
    user_created=login.user_data(name,dname,password)
    return db.validate(user_created)"""


    
def check_new_user():
    flag=input("\n\nAre you a new user\n\n")
    if (flag[0]=="Y" or flag[0]=="y"):
        user_data=getSignUpdetails()
        db.insert_into_database(user_data)
    elif (flag[0]=="N" or flag[0]=="n"):
        user_data=getLoginDetails()
    if user_data!=0:
        print("\n\nconnected successfully \n\n")
    else:
        print("\n\nconnection unsuccessful . Try Again\n\n")
        check_new_user()
    return user_data



