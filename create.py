import mysql.connector
from mysql.connector import Error

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

def create_weather_record():
    """Create a new weather record in the database."""
    location = input("Enter location: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Validate date range
    if start_date > end_date:
        print("Error: Start date cannot be after end date.")
        return

    # Collect weather data
    try:
        temperature = float(input("Enter temperature: "))
        humidity = float(input("Enter humidity: "))
        wind_speed = float(input("Enter wind speed: "))
        description = input("Enter weather description: ")

        # Insert into database
        connection = get_db_connection()
        if connection is None:
            print("Failed to connect to the database.")
            return

        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO weather_data (location, start_date, end_date, temperature, humidity, wind_speed, description)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (location, start_date, end_date, temperature, humidity, wind_speed, description))
        connection.commit()

        print("Weather record added successfully!")
    except ValueError:
        print("Invalid input for temperature, humidity, or wind speed. Please enter numeric values.")
    except Error as e:
        print(f"Database error: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Example usage
if __name__ == "__main__":
    create_weather_record()
