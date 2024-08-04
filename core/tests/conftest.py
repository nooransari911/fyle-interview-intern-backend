#import pytest
import json
from core.server import app


#@pytest.fixture
#@pytest.fixture
h_student_1 = {
        'X-Principal': json.dumps({
            'student_id': 1,
            'user_id': 1
        })
    }



#@pytest.fixture
h_student_2 = {
        'X-Principal': json.dumps({
            'student_id': 2,
            'user_id': 2
        })
    }


#@pytest.fixture
h_teacher_1 = {
        'X-Principal': json.dumps({
            'teacher_id': 1,
            'user_id': 3
        })
    }


#@pytest.fixture
h_teacher_2 = {
        'X-Principal': json.dumps({
            'teacher_id': 2,
            'user_id': 4
        })
    }


#@pytest.fixture
h_principal = {
        'X-Principal': json.dumps({
            'principal_id': 1,
            'user_id': 5
        })
    }
