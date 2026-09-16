from src.database.db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
SELECT table_name 
FROM information_schema.tables
WHERE table_schema='public'
""")

tables = cursor.fetchall()

print("Tables in PostgreSQL:")
for table in tables:
    print(table[0])

conn.close()