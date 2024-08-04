from conftest import h_student_1, h_student_2
from core.server import app
from conftest import h_principal
from core.tests.init_table import init_table
import requests, json


client=app.test_client()

def test_get_assignments_student_1 (h_student_1):
    response = (requests.get(
        'http://0.0.0.0:7755/student/assignments',
        headers=h_student_1
    ))
    data = response.json()
    datastr = json.dumps(data)
    print(f"\nStudent 1 get 1: {response.status_code}//{datastr}")
    assert response.status_code == 200

    for x in data["data"]:
        assert x['student_id'] == 1


def test_get_assignments_student_2(h_student_2):
    response = requests.get(
        'http://0.0.0.0:7755/student/assignments',
        headers=h_student_2
    )

    data = response.json()
    datastr = json.dumps(data)
    print(f"\nStudent 2 get 1: {response.status_code}//{datastr}")
    assert response.status_code == 200

    for x in data ["data"]:
        assert x ['student_id'] == 2


def test_post_assignment_null_content(h_student_1):
    """
    failure case: content cannot be null
    """

    response = requests.post(
        'http://0.0.0.0:7755/student/assignments',
        headers=h_student_1,
        json={
            'content': None
        })

    data = response.json()
    datastr = json.dumps(data)
    print(f"\nStudent 1 resubmit 1: {response.status_code}//{datastr}")

    assert response.status_code == 400
    assert data['error'] == 'FyleError'
    assert data["message"] == "assignment with empty content cannot be submitted"


def test_post_assignment_student_1(h_student_1):
    content = 'ABCD TESTPOST'

    response = requests.post(
        'http://0.0.0.0:7755/student/assignments',
        headers=h_student_1,
        json={
            'content': content
        })
    #print (response.json())

    data = response.json()
    datastr = json.dumps (data)
    print (f"\nStudent 1 post 1: {response.status_code}//{datastr}")
    assert response.status_code == 200
    assert data["data"]['content'] == content
    assert data["data"]['state'] == 'DRAFT'
    assert data["data"]['teacher_id'] is None


def test_submit_assignment_student_1(h_student_1, aid):
    response = requests.post(
        'http://0.0.0.0:7755/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': aid,
            'teacher_id': 2
        })


    data = response.json()
    datastr = json.dumps(data)
    print(f"\nStudent 1 submit 1: {response.status_code}//{datastr}")
    assert response.status_code == 200
    assert data["data"]['student_id'] == 1
    assert data["data"]['state'] == 'SUBMITTED'
    assert data["data"]['teacher_id'] == 2


def test_assignment_resubmit_error(h_student_1, aid):
    response = requests.post(
        'http://0.0.0.0:7755/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': aid,
            'teacher_id': 2
        })
    data = response.json()
    datastr = json.dumps(data)
    print(f"\nStudent 1 resubmit 1: {response.status_code}//{datastr}")

    assert response.status_code == 400
    assert data['error'] == 'FyleError'
    assert data["message"] == 'assignment cannot be resubmitted'



if (__name__ == "__main__"):
    init_table ()
    test_post_assignment_student_1(h_student_1)
    test_submit_assignment_student_1(h_student_1, 1)
    test_assignment_resubmit_error(h_student_1, 1)
    print ("\n\npart 1 success")

    test_post_assignment_null_content(h_student_1)
    test_get_assignments_student_1(h_student_1)
    test_get_assignments_student_2(h_student_2)