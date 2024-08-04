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

Student 1 post 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.479245", "grade": null, "id": 1, "state": "DRAFT", "student_id": 1, "teacher_id": null, "updated_at": "2024-08-04T19:20:44.479251"}}

Student 1 submit 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.479245", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.489635"}}

Student 1 resubmit 1: 400//{"error": "FyleError", "message": "assignment cannot be resubmitted"}

Student 1 resubmit 1: 400//{"error": "FyleError", "message": "assignment with empty content cannot be submitted"}

Student 1 get 1: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.479245", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.489635"}]}

Student 2 get 1: 200//{"data": []}


Student testing success

Teacher 2 get 1: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.479245", "grade": null, "id": 1, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.489635"}]}

Teacher 2 grade 1: 400//{"error": "FyleError", "message": "assignment was submitted to different teacher"}

Teacher 1 grade fail 1: 400//{"error": "ValidationError", "message": {"grade": ["Invalid enum member AB"]}}

Teacher 2 grade fail 1: 404//{"error": "FyleError", "message": "No assignment with this id was found"}

Student 1 post 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.538207", "grade": null, "id": 2, "state": "DRAFT", "student_id": 1, "teacher_id": null, "updated_at": "2024-08-04T19:20:44.538212"}}

Teacher 2 grade fail 2: 400//{"error": "FyleError", "message": "assignment was submitted to different teacher"}


Teacher testing success

Teacher 2 grade 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.479245", "grade": "A", "id": 1, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.557953"}}

Student 1 submit 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.538207", "grade": null, "id": 2, "state": "SUBMITTED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.568613"}}

Teacher 2 grade 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.538207", "grade": "A", "id": 2, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.579097"}}


Initial pr get all

Principal get: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.479245", "grade": "A", "id": 1, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.557953"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.538207", "grade": "A", "id": 2, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.579097"}]}


st 2 post

Student 1 post 1: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.597105", "grade": null, "id": 3, "state": "DRAFT", "student_id": 2, "teacher_id": null, "updated_at": "2024-08-04T19:20:44.597111"}}

Principal get: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.479245", "grade": "A", "id": 1, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.557953"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.538207", "grade": "A", "id": 2, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.579097"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.597105", "grade": null, "id": 3, "state": "DRAFT", "student_id": 2, "teacher_id": null, "updated_at": "2024-08-04T19:20:44.597111"}]}


st 1 post; pr grade a1 to C

Principal grade fail: 400//{"error": "FyleError", "message": "only submitted/graded assignment can be graded"}

Principal grade: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.479245", "grade": "C", "id": 1, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.618175"}}

Principal get: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.479245", "grade": "C", "id": 1, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.618175"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.538207", "grade": "A", "id": 2, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.579097"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.597105", "grade": null, "id": 3, "state": "DRAFT", "student_id": 2, "teacher_id": null, "updated_at": "2024-08-04T19:20:44.597111"}]}

pr regrade a2 to B

Principal regrade: 200//{"data": {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.538207", "grade": "B", "id": 2, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.633045"}}

Principal get: 200//{"data": [{"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.479245", "grade": "C", "id": 1, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.618175"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.538207", "grade": "B", "id": 2, "state": "GRADED", "student_id": 1, "teacher_id": 2, "updated_at": "2024-08-04T19:20:44.633045"}, {"content": "ABCD TESTPOST", "created_at": "2024-08-04T19:20:44.597105", "grade": null, "id": 3, "state": "DRAFT", "student_id": 2, "teacher_id": null, "updated_at": "2024-08-04T19:20:44.597111"}]}
(venv) (base) bash-5.2$ 
