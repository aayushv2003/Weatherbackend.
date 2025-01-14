import mysql.connector
from mysql.connector import Error
import csv

def get_db_connection():
    """Establish a database connection."""
    try:
        connection = mysql.connector.connect(
                        host='localhost',
            user='root',
            password='ayushsql123',
            database='weather_app'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def export_to_csv():
    """Export weather data records to a CSV file."""
    connection = get_db_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM weather_data")
        records = cursor.fetchall()

        if not records:
            print("No records found to export.")
            return

        # Writing data to CSV file
        with open("weather_data.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=records[0].keys())
            writer.writeheader()
            writer.writerows(records)

        print("Data exported to weather_data.csv")

    except Error as e:
        print(f"Database error: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage
if __name__ == "__main__":
    export_to_csv()
