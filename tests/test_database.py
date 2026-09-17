from src.database.db import get_connection


def test_database_connection():

    conn = get_connection()

    assert conn is not None

    conn.close()
