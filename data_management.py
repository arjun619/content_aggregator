import psycopg2
from random import randint
from login import user_data
import datetime
def db_connect():
    con=psycopg2.connect(
    host="127.0.0.1",
    database="userdata",
    user="postgres",
    password=4769516619
    )
    return con
#count=randint(1,1000000)


def insert_into_database(user_info):
   con=db_connect()
   cur=con.cursor() 
   #global count
   cur.execute("insert into logindetails(user_id,full_name,display_name,password) values(%s,%s,%s,%s)",(user_info.user_id,user_info.name,user_info.display_name,user_info.password))
   con.commit() 
   cur.close()
   con.close()

def validate(name,dname,password):
    con=db_connect()
    cur=con.cursor()
    cur.execute("select * from logindetails")
    #print(type(data.name),type(data.display_name),type(data.password))
    for i in cur:
        #print(type(i[0]),type(i[1]),type(i[2]))
        if i[0]==name and i[1]==dname and int(i[2])==int(password):
            data=user_data(i[0],i[1],i[2],i[3])

            return data
    return 0

def history_store(user_data,data):
    con=db_connect()
    cur=con.cursor()
    id=user_data.user_id
    url=data
    time=datetime.datetime.now()
    year=time.year
    month=str(time.month)
    day=str(time.month)
    if len(month)==1:
        month=f"0{month}"
    if len(day)==1:
        day=f"0{month}"
    date=f"{year}-{month}-{day}"
    cur.execute("insert into history(user_id,url,time) values (%s,%s,%s)",(id,url,date))
    con.commit()
    cur.close()
    con.close()

def view_history(name):
    flag=input("Do you want to view your history before exitting ?\n")
    if (flag[0]=='y' or flag[0]=="Y"):
        con=db_connect()
        cur=con.cursor()
        name=str(name)
        query=f"select url,time from history,logindetails as ld where ld.full_name='{name}' and ld.user_id=history.user_id"
        cur.execute(query)
        records=cur.fetchall()
        for url,date in records:
            print(url,date)
        cur.close()
        con.close()
    else:
        return
    
    

