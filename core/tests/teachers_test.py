from conftest import h_teacher_1, h_teacher_2, h_student_2, h_student_1
import json, requests
from init_table import init_table
import students_test
from core.models.assignments import GradeEnum

def test_get_assignments_teacher_1(h_teacher_1):
    response = requests.get(
        '/teacher/assignments',
        headers=h_teacher_1
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['teacher_id'] == 1


def test_get_assignments_teacher_2(h_teacher_2):
    response = requests.get(
        'http://0.0.0.0:7755/teacher/assignments',
        headers=h_teacher_2
    )

    data = response.json()
    datastr = json.dumps(data)
    print(f"\nTeacher 2 get 1: {response.status_code}//{datastr}")
    assert response.status_code == 200

    for x in data["data"]:
        assert x['teacher_id'] == 2
        assert x['state'] in ['SUBMITTED', 'GRADED']



def test_grade_assignment_cross(h_teacher_1):
    """
    failure case: assignment 1 was submitted to teacher 2 and not teacher 1
    """
    response = requests.post(
        'http://0.0.0.0:7755/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 1,
            "grade": "A"
        }
    )
    data = response.json()
    datastr = json.dumps(data)
    print(f"\nTeacher 2 grade 1: {response.status_code}//{datastr}")
    assert response.status_code == 400

    assert data['error'] == 'FyleError'


def test_grade_assignment_bad_grade(h_teacher_2):
    """
    failure case: API should allow only grades available in enum
    """
    response = requests.post(
        'http://0.0.0.0:7755/teacher/assignments/grade',
        headers=h_teacher_2,
        json={
            "id": 1,
            "grade": "AB"
        }
    )
    data = response.json()
    datastr = json.dumps(data)
    print(f"\nTeacher 1 grade fail 1: {response.status_code}//{datastr}")
    assert response.status_code == 400

    assert data['error'] == 'ValidationError'


def test_grade_assignment_bad_assignment(h_teacher_2):
    """
    failure case: If an assignment does not exists check and throw 404
    """
    response = requests.post(
        'http://0.0.0.0:7755/teacher/assignments/grade',
        headers=h_teacher_2,
        json={
            "id": 100000,
            "grade": "A"
        }
    )
    data = response.json()
    datastr = json.dumps(data)
    print(f"\nTeacher 2 grade fail 1: {response.status_code}//{datastr}")
    assert response.status_code == 404

    assert data['error'] == 'FyleError'


def test_grade_assignment_draft_assignment(h_teacher_2):
    """
    failure case: only a submitted assignment can be graded
    """
    response = requests.post(
        'http://0.0.0.0:7755/teacher/assignments/grade',
        headers=h_teacher_2
        , json={
            "id": 2,
            "grade": "A"
        }
    )
    data = response.json()
    datastr = json.dumps(data)
    print(f"\nTeacher 2 grade fail 2: {response.status_code}//{datastr}")
    assert response.status_code == 400

    assert data['error'] == 'FyleError'


def test_grade_assignment(h_teacher_2, aid):
    response = requests.post(
        'http://0.0.0.0:7755/teacher/assignments/grade',
        json={
            'id': aid,
            'grade': GradeEnum.A.value
        },
        headers=h_teacher_2
    )
    data = response.json()
    datastr = json.dumps(data)
    print(f"\nTeacher 2 grade 1: {response.status_code}//{datastr}")
    assert response.status_code == 200



if (__name__ == "__main__"):
    init_table()
    students_test.test_post_assignment_student_1(h_student_1)
    students_test.test_submit_assignment_student_1(h_student_1, 1)
    students_test.test_assignment_resubmit_error(h_student_1, 1)

    students_test.test_post_assignment_null_content(h_student_1)
    students_test.test_get_assignments_student_1(h_student_1)
    students_test.test_get_assignments_student_2(h_student_2)
    print("\n\nStudent testing success")


    test_get_assignments_teacher_2(h_teacher_2)
    test_grade_assignment_cross(h_teacher_1)
    test_grade_assignment_bad_grade(h_teacher_2)
    test_grade_assignment_bad_assignment(h_teacher_2)
    students_test.test_post_assignment_student_1(h_student_1)
    #students_test.test_submit_assignment_student_1(h_student_1, 2)
    test_grade_assignment_draft_assignment(h_teacher_2)
    print("\n\nTeacher testing success")