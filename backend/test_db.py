import mysql.connector

def test_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="Sagar@1234",  # Replace with your MySQL password
            database="DBChatbot_db"
        )
        if conn.is_connected():
            print("Database connection successful!")
        else:
            print("Database connection failed.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

test_db_connection()
