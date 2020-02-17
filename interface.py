import sys
import login
import utility_funcs
flag=input("Do you want to enter the content aggregator ")
if flag[0]=="N" or flag=="n":
    exit()

user_flag=input("Are you a new user ")
if user_flag[0]=="y" or user_flag[0]=="Y":
    new_user=utility_funcs.getlogindetails()
utility_funcs.menu()
interest=input()
if interest=="1":
    
     


