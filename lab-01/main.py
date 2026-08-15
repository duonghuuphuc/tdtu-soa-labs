# Exercise 3
# To run the application: uvicorn main:app --reload --port 8081
# Swagger UI: http://127.0.0.1:8081/docs

from fastapi import FastAPI, HTTPException

## (1) Define app
app = FastAPI(
    title="Student Service",
    description="A simple FastAPI application for managing students.",
    version="1.0.0"
)


## (2) Prepare data
students = [
    {"student_id": "S001", "name": "An Nguyen", "age": 20, "email": "an@example.com", "gpa": 3.5},
    {"student_id": "S002", "name": "Binh Tran", "age": 22, "email": "binh@example.com", "gpa": 3.8},
    {"student_id": "S003", "name": "Hoa Pham", "age": 21, "email": "hoa@example.com", "gpa": 3.2}
]


## (3) Define endpoints

@app.get("/")
def root():
    return {"service": "Student Service", "course": "504070"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: str):
    for s in students:
        if s["student_id"] == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")