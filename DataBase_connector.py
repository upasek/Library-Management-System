import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='LibraryManagementSystem'
)
