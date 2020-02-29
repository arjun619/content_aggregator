import sys
import login
import utility_funcs
import scrapping
import data_management
flag=input("Do you want to enter the content aggregator ")
if flag[0]=="N" or flag=="n":
    exit()

user_data=utility_funcs.check_new_user()
utility_funcs.menu()
interest=int(input())
while (interest!=0):
    if interest==1 :
        data=scrapping.data_science_scrap()
        utility_funcs.link_display(user_data,data)
    elif interest==2:
        data=scrapping.football_scrap()
        utility_funcs.link_display(user_data,data)
    utility_funcs.menu()
    interest=int(input())

data_management.view_history(user_data.name)



    
    
     


