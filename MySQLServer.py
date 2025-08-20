import mysql.connector
from mysql.connector import Error
def create_database():
    try:
        mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "123MeDo4564@")
        if mydb.is_connected():
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            mycursor.close()
            mydb.close()
            print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error: Could not connect to MySQL server. {e}")
    

create_database()