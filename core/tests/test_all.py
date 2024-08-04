import os, subprocess


test_files = [
    "python3 /home/ansarimn/Downloads/fyle-interview-intern-backend/tests/students_test.py",
    "echo \"Students test completed\"",
    "python3 /home/ansarimn/Downloads/fyle-interview-intern-backend/tests/teachers_test.py",
    "echo \"Teachers test completed\"",
    "python3 /home/ansarimn/Downloads/fyle-interview-intern-backend/tests/principals_test.py"
    "echo \"Principals test completed\"",
]

[subprocess.Popen (i, shell=True).wait () for i in test_files]