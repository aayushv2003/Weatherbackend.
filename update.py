import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
         host='localhost',
            user='root',
            password='ayushsql123',
            database='weather_app'
    )

def update_weather_record(record_id, field, new_value):
    # Get the database connection
    connection = get_db_connection()
    cursor = connection.cursor()

    # Prepare the SQL query for updating the record
    query = f"UPDATE weather_data SET {field} = %s WHERE id = %s"
    
    try:
        # Execute the query with the new value and record ID
        cursor.execute(query, (new_value, record_id))
        
        # Commit the changes
        connection.commit()
        
        # Check if any record was updated
        if cursor.rowcount > 0:
            print("Record updated successfully!")
        else:
            print("No record found with the given ID.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        # Close the cursor and the connection
        cursor.close()
        connection.close()

# Example usage
update_weather_record(1, "temperature", 30)  # Example: Update temperature for record with ID 1
