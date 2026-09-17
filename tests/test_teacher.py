from src.database.db import (
    create_teacher,
    teacher_login,
    get_connection
)


def cleanup_teacher():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM teachers WHERE username = %s",
        ("test_teacher",)
    )

    conn.commit()
    conn.close()


def test_teacher_creation():

    cleanup_teacher()

    result = create_teacher(
        "test_teacher",
        "12345",
        "Test Teacher"
    )

    assert result


def test_teacher_login():

    teacher = teacher_login(
        "test_teacher",
        "12345"
    )

    assert teacher is not None
