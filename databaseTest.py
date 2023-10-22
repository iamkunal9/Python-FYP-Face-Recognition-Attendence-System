import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='face_recognition'
)

print(mydb)
# conn = mysql.connector.connect('root','','localhost','face_recognition',3307)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()