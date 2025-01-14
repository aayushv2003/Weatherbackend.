import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Establish a database connection."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ayushsql123',
            database='weather_app'  # replace with your database name
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def read_weather_records():
    """Retrieve all weather records from the database."""
    connection = get_db_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM weather_data")
        records = cursor.fetchall()

        if not records:
            print("No records found.")
        else:
            print("Weather Records:")
            for record in records:
                print(record)

    except Error as e:
        print(f"Database error: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage
if __name__ == "__main__":
    read_weather_records()
