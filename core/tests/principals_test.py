from core.models.assignments import AssignmentStateEnum, GradeEnum
from core.server import app
from headers import h_principal, h_student_2, h_student_1, h_teacher_1, h_teacher_2
from conftest import assert_all
import requests, json
import students_test, teachers_test
from init_table import init_table
import sys, os
import pytest

client=app.test_client()

@pytest.mark.skip
def test_get_assignments(h_principal):
    response = requests.get(
        'http://0.0.0.0:7755/principal/assignments',
        headers=h_principal
    )

    data = response.json()
    datastr = json.dumps(data)
    print(f"\nPrincipal get request: {response.status_code}//{datastr}")
    assert response.status_code == 200
    return response


@pytest.mark.skip
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
    print(f"\nPrincipal grade fail: draft assignment: {response.status_code}//{datastr}")
    assert response.status_code == 400

@pytest.mark.skip
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

@pytest.mark.skip
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


@pytest.mark.skip
def test_all_functions_1():
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

    print("\n\nInitial principal get all")
    test_get_assignments(h_principal)

    students_test.test_post_assignment_student_1(h_student_2)
    test_get_assignments(h_principal)

    test_grade_assignment_draft_assignment(h_principal)
    test_grade_assignment(h_principal)
    test_get_assignments(h_principal)

    test_regrade_assignment(h_principal)
    test_get_assignments(h_principal)

@pytest.mark.usefixtures("assert_all")
def test_all_functions_2 (assert_all):
    test_all_functions_1()

    response = test_get_assignments(h_principal)
    data = response.json()
    datastr = json.dumps(data)
    print(f"\nPrincipal last get request: {response.status_code}//{datastr}")


    #response_assert_all = assert_all ()
    for i in [0, 1, 2]:
        assert data["data"][i]["id"] == assert_all[i]["id"]
        assert data["data"][i]["student_id"] == assert_all[i]["student_id"]
        assert data["data"][i]["teacher_id"] == assert_all[i]["teacher_id"]
        assert data["data"][i]["state"] == assert_all[i]["state"]
        assert data["data"][i]["grade"] == assert_all[i]["grade"]

    '''
    assert data["data"][0]["id"] == assert_all [0]["id"]
    assert data["data"][1]["id"] == assert_all [1]["id"]
    assert data["data"][2]["id"] == assert_all [2]["id"]

    assert data["data"][0]["student_id"] == assert_all[0]["student_id"]
    assert data["data"][1]["student_id"] == assert_all[1]["student_id"]
    assert data["data"][2]["student_id"] == assert_all[2]["student_id"]
    '''




if (__name__ == "__main__"):
    test_all_functions_1 ()