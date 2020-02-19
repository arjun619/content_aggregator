import psycopg2
from random import randint
from login import user_data
"""con=psycopg2.connect(
    host="127.0.0.1",
    database="userdata",
    user="postgres",
    password=4769516619
    )"""
count=randint(1,1000000)


def insert_into_database(user_info):
   con=psycopg2.connect(
   host="127.0.0.1",
   database="userdata",
   user="postgres",
   password=4769516619
   )
   cur=con.cursor() 
   global count
   count+=1
   cur.execute("insert into logindetails(user_id,full_name,display_name,password) values(%s,%s,%s,%s)",(count,user_info.name,user_info.display_name,user_info.password))
   con.commit() 
   
   cur.close()
   con.close()
   
#cur.execute("select * from logindetails")  


