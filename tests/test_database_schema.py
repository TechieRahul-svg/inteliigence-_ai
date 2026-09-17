from src.database.db import get_connection, setup_database


def test_tables_created():

    setup_database()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables
        WHERE table_schema='public'
    """)

    tables = [
        row[0] for row in cursor.fetchall()
    ]

    assert "teachers" in tables
    assert "students" in tables
    assert "subjects" in tables
    assert "attendance_logs" in tables

    conn.close()