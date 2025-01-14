import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
            user='root',
            password='ayushsql123',
            database='weather_app'
    )

def delete_weather_record():
    # Get the record ID to delete from the user
    record_id = int(input("Enter the record ID to delete: "))

    # Connect to the database
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Prepare the delete query
        query = "DELETE FROM weather_data WHERE id = %s"
        
        # Execute the delete query with the provided record ID
        cursor.execute(query, (record_id,))
        
        # Commit the changes to delete the record
        connection.commit()
        
        # Check if any record was deleted
        if cursor.rowcount > 0:
            print("Weather record deleted successfully!")
        else:
            print("No record found with the given ID.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Example usage
delete_weather_record()
