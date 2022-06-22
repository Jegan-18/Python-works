import mysql.connector as conn

mydb = conn.connect(host='localhost', user='root', passwd='12345', database="usersdb")

mycursor = mydb.cursor()

mycursor.execute("select * from users")

result = mycursor.fetchall()

for i in result:
    print(i)