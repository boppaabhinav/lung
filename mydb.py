import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="Abhinav@18",database="bank")
cur=mydb.cursor()
s="drop table manager"
cur.execute(s)
