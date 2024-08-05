import pytest
import json
from core.server import app


@pytest.fixture
def assert_all ():
    return (
        [
            {
                "id": 1,
                "student_id": 1,
                "teacher_id": 2,
                "state": "GRADED",
                "grade": "C"
            },
            {
                "id": 2,
                "student_id": 1,
                "teacher_id": 2,
                "state": "GRADED",
                "grade": "B"
            },
            {
                "id": 3,
                "student_id": 2,
                "teacher_id": None,
                "state": "DRAFT",
                "grade": None
            }
        ]
    )
