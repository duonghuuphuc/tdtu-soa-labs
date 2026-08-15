# Exercise 2
# Require: pip install 'pydantic[email]'

from pydantic import BaseModel, EmailStr, Field, ValidationError

## (1) Define Student class
class Student(BaseModel):
    student_id: str = Field(min_length=1)
    name: str = Field(min_length=2)
    age: int = Field(ge=18, le=60)
    email: EmailStr
    gpa: float = Field(ge=0.0, le=4.0)


## (2) Prepare data
student_data = [
    {"student_id": "S001", "name": "An Nguyen", "age": 20, "email": "an@example.com", "gpa": 3.5},
    {"student_id": "S002", "name": "Binh Tran", "age": 22, "email": "binh@example.com", "gpa": 3.8},
    {"student_id": "", "name": "Chi Le", "age": 21, "email": "chi@example.com", "gpa": 3.2},
    {"student_id": "S004", "name": "D", "age": 17, "email": "invalid-email", "gpa": 4.5},
    {"student_id": "S005", "name": "Hoa Pham", "age": 25, "email": "hoa@example.com", "gpa": 2.9}
]

valid_students = []
invalid_students = []


## (3) Processing
for data in student_data:
    try:
        student = Student(**data)
        valid_students.append(student)
    except ValidationError as error:
        invalid_students.append(
            {
                "data": data,
                "errors": error.errors()
            }
        )


## (4) Print
print(f"Number of valid students: {len(valid_students)}")
print(f"Number of invalid students: {len(invalid_students)}")

print("\nValid Students:")
for student in valid_students:
    print(student)

print("\nInvalid Students:")
for student in invalid_students:
    print(f"Data: {student['data']}")

    for error in student["errors"]:
        field = error["loc"][0]
        message = error["msg"]
        print(f"- {field}: {message}")