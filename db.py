import mysql.connector

# Returns a MySQL connection object
def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "YOUR_PASSWORD",
        database = "YOUR_DATABSE_NAME"
    )