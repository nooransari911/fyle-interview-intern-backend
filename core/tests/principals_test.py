from core.models.assignments import AssignmentStateEnum, GradeEnum
from core.server import app
from conftest import h_principal
import requests, json
import students_test, teachers_test
from conftest import h_principal, h_student_2, h_student_1, h_teacher_1, h_teacher_2
from init_table import init_table

client=app.test_client()

def test_get_assignments(h_principal):
    response = requests.get(
        'http://0.0.0.0:7755/principal/assignments',
        headers=h_principal
    )

    data = response.json()
    datastr = json.dumps(data)
    print(f"\nPrincipal get: {response.status_code}//{datastr}")
    assert response.status_code == 200



def test_grade_assignment_draft_assignment(h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    response = requests.post(
        'http://0.0.0.0:7755/principal/assignments/grade',
        json={
            'id': 3,
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )
    data = response.json()
    datastr = json.dumps(data)
    print(f"\nPrincipal grade fail: {response.status_code}//{datastr}")
    assert response.status_code == 400


def test_grade_assignment(h_principal):
    response = requests.post(
        'http://0.0.0.0:7755/principal/assignments/grade',
        json={
            'id': 1,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )
    data = response.json()
    datastr = json.dumps(data)
    print(f"\nPrincipal grade: {response.status_code}//{datastr}")
    assert response.status_code == 200

    assert data['data']['state'] == AssignmentStateEnum.GRADED.value
    assert data['data']['grade'] == GradeEnum.C.value


def test_regrade_assignment(h_principal):
    response = requests.post(
        'http://0.0.0.0:7755/principal/assignments/grade',
        json={
            'id': 2,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )
    data = response.json()
    datastr = json.dumps(data)
    print(f"\nPrincipal regrade: {response.status_code}//{datastr}")
    assert response.status_code == 200

    assert data['data']['state'] == AssignmentStateEnum.GRADED.value
    assert data['data']['grade'] == GradeEnum.B.value



if (__name__ == "__main__"):
    init_table()
    students_test.test_post_assignment_student_1(h_student_1)
    students_test.test_submit_assignment_student_1(h_student_1, 1)
    students_test.test_assignment_resubmit_error(h_student_1, 1)

    students_test.test_post_assignment_null_content(h_student_1)
    students_test.test_get_assignments_student_1(h_student_1)
    students_test.test_get_assignments_student_2(h_student_2)
    print("\n\nStudent testing success")

    teachers_test.test_get_assignments_teacher_2(h_teacher_2)
    teachers_test.test_grade_assignment_cross(h_teacher_1)
    teachers_test.test_grade_assignment_bad_grade(h_teacher_2)
    teachers_test.test_grade_assignment_bad_assignment(h_teacher_2)
    students_test.test_post_assignment_student_1(h_student_1)
    # students_test.test_submit_assignment_student_1(h_student_1, 2)
    teachers_test.test_grade_assignment_draft_assignment(h_teacher_2)
    print("\n\nTeacher testing success")

    teachers_test.test_grade_assignment(h_teacher_2, 1)

    students_test.test_submit_assignment_student_1(h_student_1, 2)
    teachers_test.test_grade_assignment(h_teacher_2, 2)



    print ("\n\nInitial pr get all")
    test_get_assignments(h_principal)

    print("\n\nst 2 post")
    students_test.test_post_assignment_student_1(h_student_2)
    test_get_assignments(h_principal)

    print("\n\nst 1 post; pr grade a1 to C")
    test_grade_assignment_draft_assignment(h_principal)
    test_grade_assignment(h_principal)
    test_get_assignments(h_principal)

    print("\npr regrade a2 to B")
    test_regrade_assignment(h_principal)
    test_get_assignments(h_principal)