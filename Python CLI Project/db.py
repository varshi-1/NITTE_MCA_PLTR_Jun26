import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Varshitha@123",
        database="hostel_db"
    )
