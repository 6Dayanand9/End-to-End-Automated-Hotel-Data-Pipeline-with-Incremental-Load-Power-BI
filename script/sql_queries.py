import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="food_data_model"
    )

def get_row_count():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM fact_orders")
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count