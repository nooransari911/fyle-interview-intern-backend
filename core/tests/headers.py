import json


h_student_1 = {
        'X-Principal': json.dumps({
            'student_id': 1,
            'user_id': 1
        })
    }




h_student_2 = {
        'X-Principal': json.dumps({
            'student_id': 2,
            'user_id': 2
        })
    }



h_teacher_1 = {
        'X-Principal': json.dumps({
            'teacher_id': 1,
            'user_id': 3
        })
    }


h_teacher_2 = {
        'X-Principal': json.dumps({
            'teacher_id': 2,
            'user_id': 4
        })
    }


h_principal = {
        'X-Principal': json.dumps({
            'principal_id': 1,
            'user_id': 5
        })
    }