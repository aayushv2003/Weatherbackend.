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


def create_weather_record():
    """Create a new weather record in the database."""
    location = input("Enter location: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Validate date range
    if start_date > end_date:
        print("Error: Start date cannot be after end date.")
        return

    try:
        temperature = float(input("Enter temperature: "))
        humidity = float(input("Enter humidity: "))
        wind_speed = float(input("Enter wind speed: "))
        description = input("Enter weather description: ")

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


def read_weather_records():
    """Retrieve and display all weather records from the database."""
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


def update_weather_record():
    """Update an existing weather record in the database."""
    record_id = input("Enter the ID of the record to update: ")
    try:
        temperature = float(input("Enter new temperature: "))
        humidity = float(input("Enter new humidity: "))
        wind_speed = float(input("Enter new wind speed: "))
        description = input("Enter new weather description: ")

        connection = get_db_connection()
        if connection is None:
            print("Failed to connect to the database.")
            return

        cursor = connection.cursor()
        cursor.execute("""
            UPDATE weather_data
            SET temperature = %s, humidity = %s, wind_speed = %s, description = %s
            WHERE id = %s
        """, (temperature, humidity, wind_speed, description, record_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("Weather record updated successfully!")
        else:
            print("No record found with the given ID.")
    except ValueError:
        print("Invalid input for temperature, humidity, or wind speed. Please enter numeric values.")
    except Error as e:
        print(f"Database error: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


def delete_weather_record():
    """Delete a weather record from the database."""
    record_id = input("Enter the ID of the record to delete: ")
    connection = get_db_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM weather_data WHERE id = %s", (record_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Weather record deleted successfully!")
        else:
            print("No record found with the given ID.")
    except Error as e:
        print(f"Database error: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


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


def main():
    """Main menu-driven interface for the weather application."""
    while True:
        print("\nWeather Data Management System")
        print("1. Create Weather Record")
        print("2. Read Weather Records")
        print("3. Update Weather Record")
        print("4. Delete Weather Record")
        print("5. Export Weather Records to CSV")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_weather_record()
        elif choice == "2":
            read_weather_records()
        elif choice == "3":
            update_weather_record()
        elif choice == "4":
            delete_weather_record()
        elif choice == "5":
            export_to_csv()
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
