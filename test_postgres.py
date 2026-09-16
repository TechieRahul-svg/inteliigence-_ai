from src.database.db import get_connection


print("Starting connection test...")

try:
    conn = get_connection()

    print("PostgreSQL Connected Successfully")

    conn.close()

except Exception as e:
    print("Connection Failed:")
    print(e)