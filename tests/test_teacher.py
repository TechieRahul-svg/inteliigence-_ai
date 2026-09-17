from src.database.db import create_teacher, teacher_login


def test_teacher_creation():

    result = create_teacher(
        "test_teacher",
        "12345",
        "Test Teacher"
    )

    assert result == True


def test_teacher_login():

    teacher = teacher_login(
        "test_teacher",
        "12345"
    )

    assert teacher is not None