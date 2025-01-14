import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        print("Attempting to connect to the database...")  # Debugging message
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         # Replace with your actual username
            password="ayushsql123", # Replace with your actual password
            database="weather_app"     # Replace with your database name
        )
        if connection.is_connected():
            print("Database connected successfully!")  # Message on successful connection
            return connection
    except Error as e:
        print(f"Error: Could not connect to the database. Details: {e}")  # Log the error
        return None
    finally:
        print("Connection attempt completed.")  # Always logs after the attempt

# Test the connection
if __name__ == "__main__":
    connection = get_db_connection()
    if connection:
        print("Connection object created. Proceeding with other operations...")
        connection.close()
        print("Connection closed.")
    else:
        print("Connection attempt failed.")
