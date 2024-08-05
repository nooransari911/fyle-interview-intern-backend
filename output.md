# Pytest run 1
=================================================== test session starts ====================================================
platform linux -- Python 3.11.5, pytest-8.3.2, pluggy-1.5.0
rootdir: /home/ansarimn/Downloads/fyle-interview-intern-backend
configfile: pytest.ini
plugins: cov-2.12.1
collected 19 items

core/tests/principals_test.py sssss.                                                                                 [ 31%]
core/tests/students_test.py ssssss                                                                                   [ 63%]
core/tests/teachers_test.py sssssss                                                                                  [100%]

---------- coverage: platform linux, python 3.11.5-final-0 -----------
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
core/__init__.py                        20      0   100%
core/apis/__init__.py                    0      0   100%
core/apis/assignments/__init__.py        3      1    67%
core/apis/assignments/principal.py      26     11    58%
core/apis/assignments/schema.py         37      4    89%
core/apis/assignments/student.py        46     26    43%
core/apis/assignments/teacher.py        29     14    52%
core/apis/decorators.py                 32     18    44%
core/apis/responses.py                   6      2    67%
core/libs/__init__.py                    0      0   100%
core/libs/assertions.py                 16     10    38%
core/libs/exceptions.py                 11      7    36%
core/libs/helpers.py                    11      3    73%
core/models/__init__.py                  0      0   100%
core/models/assignments.py              91     46    49%
core/models/autoschema.py               32      1    97%
core/models/principals.py               13      2    85%
core/models/students.py                 13      2    85%
core/models/teachers.py                 20      5    75%
core/models/users.py                    24      6    75%
core/server.py                          27     11    59%
--------------------------------------------------------
TOTAL                                  457    169    63%


============================================== 1 passed, 18 skipped in 1.74s ===============================================


# Run 1: only student
## (venv) (base) bash-5.2$ python3 ./core/tests/students_test.py

Student 1 post 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T17:58:40.853442", "grade": null, "id": 2, "state": "DRAFT", "student_id": 1, "teacher_id": null, "updated_at": "2024-08-04T17:58:40.853444"}}

Student 1 submit 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T17:58:40.853442", "grade": null, "id": 2, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T17:58:40.860498"}}

Student 1 resubmit 1: 400//{"error": "FyleError", "message": "assignment cannot be resubmitted"}


part 1 success

Student 1 resubmit 1: 400//{"error": "FyleError", "message": "assignment with empty content cannot be submitted"}

Student 1 get 1: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-04T17:58:35.991874", "grade": null, "id": 1, "state": "DRAFT", "student_id": 1, "teacher_id": null, "updated_at": "2024-08-04T17:58:35.991879"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-04T17:58:40.853442", "grade": null, "id": 2, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T17:58:40.860498"}]}

Student 2 get 1: 200//{"data": []}



# Run 2: only student
## (venv) (base) bash-5.2$ python3 ./core/tests/students_test.py 

Student 1 post 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:01:37.214718", "grade": null, "id": 1, "state": "DRAFT", "student_id": 1, "teacher_id": null, "updated_at": "2024-08-04T18:01:37.214722"}}

Student 1 submit 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:01:37.214718", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T18:01:37.231126"}}

Student 1 resubmit 1: 400//{"error": "FyleError", "message": "assignment cannot be resubmitted"}


part 1 success

Student 1 resubmit 1: 400//{"error": "FyleError", "message": "assignment with empty content cannot be submitted"}

Student 1 get 1: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:01:37.214718", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T18:01:37.231126"}]}

Student 2 get 1: 200//{"data": []}


# Run3: student and teacher
## (venv) (base) bash-5.2$ python3 ./core/tests/teachers_test.py 

Student 1 post 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:40:45.307285", "grade": null, "id": 1, "state": "DRAFT", "student_id": 1, "teacher_id": null, "updated_at": "2024-08-04T18:40:45.307289"}}

Student 1 submit 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:40:45.307285", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T18:40:45.319399"}}

Student 1 resubmit 1: 400//{"error": "FyleError", "message": "assignment cannot be resubmitted"}

Student 1 resubmit 1: 400//{"error": "FyleError", "message": "assignment with empty content cannot be submitted"}

Student 1 get 1: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:40:45.307285", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T18:40:45.319399"}]}

Student 2 get 1: 200//{"data": []}


Student testing success

Teacher 2 get 1: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:40:45.307285", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T18:40:45.319399"}]}

Teacher 2 grade 1: 400//{"error": "FyleError", "message": "assignment was submitted to different teacher"}

Teacher 1 grade fail 1: 400//{"error": "ValidationError", "message": {"grade": ["Invalid enum member AB"]}}

Teacher 2 grade fail 1: 404//{"error": "FyleError", "message": "No assignment with this id was found"}

Student 1 post 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:40:45.367890", "grade": null, "id": 2, "state": "DRAFT", "student_id": 1, "teacher_id": null, "updated_at": "2024-08-04T18:40:45.367895"}}

Teacher 2 grade fail 2: 400//{"error": "FyleError", "message": "assignment was submitted to different teacher"}


Teacher testing success


# Run 4: student and teacher
## (venv) (base) bash-5.2$ python3 ./core/tests/teachers_test.py 

Student 1 post 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:53:26.670203", "grade": null, "id": 1, "state": "DRAFT", "student_id": 1, "teacher_id": null, "updated_at": "2024-08-04T18:53:26.670208"}}

Student 1 submit 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:53:26.670203", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T18:53:26.681927"}}

Student 1 resubmit 1: 400//{"error": "FyleError", "message": "assignment cannot be resubmitted"}

Student 1 resubmit 1: 400//{"error": "FyleError", "message": "assignment with empty content cannot be submitted"}

Student 1 get 1: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:53:26.670203", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T18:53:26.681927"}]}

Student 2 get 1: 200//{"data": []}


Student testing success

Teacher 2 get 1: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:53:26.670203", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T18:53:26.681927"}]}

Teacher 2 grade 1: 400//{"error": "FyleError", "message": "assignment was submitted to different teacher"}

Teacher 1 grade fail 1: 400//{"error": "ValidationError", "message": {"grade": ["Invalid enum member AB"]}}

Teacher 2 grade fail 1: 404//{"error": "FyleError", "message": "No assignment with this id was found"}

Student 1 post 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T18:53:26.730022", "grade": null, "id": 2, "state": "DRAFT", "student_id": 1, "teacher_id": null, "updated_at": "2024-08-04T18:53:26.730039"}}

Teacher 2 grade fail 2: 400//{"error": "FyleError", "message": "assignment was submitted to different teacher"}


Teacher testing success





# Run 5: All: principal, student and teacher
## (venv) (base) bash-5.2$ python3 ./core/tests/principals_test.py 

Student 1 post: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.900963", "grade": null, "id": 1, "state": "DRAFT", "student_id": 1, "teacher_id": null, "updated_at": "2024-08-05T06:27:18.900968"}}

Student 1 submit: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.900963", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:18.912274"}}

Student 1 resubmit: 400//{"error": "FyleError", "message": "assignment cannot be resubmitted"}

Student 1 submit null content: 400//{"error": "FyleError", "message": "assignment with empty content cannot be submitted"}

Student 1 get request: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.900963", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:18.912274"}]}

Student 2 get request: 200//{"data": []}


Student testing success

Teacher 2 get request: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.900963", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:18.912274"}]}

Teacher grade fail: wrong teacher: 400//{"error": "FyleError", "message": "assignment was submitted to different teacher"}

Teacher grade fail: bad grade: 400//{"error": "ValidationError", "message": {"grade": ["Invalid enum member AB"]}}

Teacher grade fail: no such assignment: 404//{"error": "FyleError", "message": "No assignment with this id was found"}

Student 1 post: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.959543", "grade": null, "id": 2, "state": "DRAFT", "student_id": 1, "teacher_id": null, "updated_at": "2024-08-05T06:27:18.959547"}}

Teacher grade fail: cannot grade draft assignment: 400//{"error": "FyleError", "message": "assignment was submitted to different teacher"}


Teacher testing success

Teacher 2 grade: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.900963", "grade": "A", "id": 1, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:18.975711"}}

Student 1 submit: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.959543", "grade": null, "id": 2, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:18.986564"}}

Teacher 2 grade: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.959543", "grade": "A", "id": 2, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:18.996763"}}


Initial principal get all

Principal get request: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.900963", "grade": "A", "id": 1, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:18.975711"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.959543", "grade": "A", "id": 2, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:18.996763"}]}

Student 1 post: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:19.011312", "grade": null, "id": 3, "state": "DRAFT", "student_id": 2, "teacher_id": null, "updated_at": "2024-08-05T06:27:19.011317"}}

Principal get request: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.900963", "grade": "A", "id": 1, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:18.975711"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.959543", "grade": "A", "id": 2, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:18.996763"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:19.011312", "grade": null, "id": 3, "state": "DRAFT", "student_id": 2, "teacher_id": null, "updated_at": "2024-08-05T06:27:19.011317"}]}

Principal grade fail: draft assignment: 400//{"error": "FyleError", "message": "only submitted/graded assignment can be graded"}

Principal grade: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.900963", "grade": "C", "id": 1, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:19.031977"}}

Principal get request: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.900963", "grade": "C", "id": 1, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:19.031977"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.959543", "grade": "A", "id": 2, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:18.996763"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:19.011312", "grade": null, "id": 3, "state": "DRAFT", "student_id": 2, "teacher_id": null, "updated_at": "2024-08-05T06:27:19.011317"}]}

Principal regrade: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.959543", "grade": "B", "id": 2, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:19.050410"}}

Principal get request: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.900963", "grade": "C", "id": 1, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:19.031977"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:18.959543", "grade": "B", "id": 2, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-05T06:27:19.050410"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-05T06:27:19.011312", "grade": null, "id": 3, "state": "DRAFT", "student_id": 2, "teacher_id": null, "updated_at": "2024-08-05T06:27:19.011317"}]}
