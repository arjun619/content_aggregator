import getpass
import login
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