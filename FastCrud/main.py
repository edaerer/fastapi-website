from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import Optional


class Course(BaseModel):
    id: int
    instructor: str
    title: str
    category: str

app = FastAPI()
courses_db = [
    {"id": 1, "instructor": "Eda", "title": "C/C++", "category": "Development"},
    {"id": 2, "instructor": "Elif", "title": "Anatomy", "category": "Medicine"},
    {"id": 3, "instructor": "Ayse", "title": "Python", "category": "Development"},
    {"id": 4, "instructor": "Nida", "title": "Dentistry", "category": "Medicine"},
    {"id": 5, "instructor": "Ozge", "title": "Generative AI", "category": "Development"},
    {"id": 6, "instructor": "Nisa", "title": "Animal Rights", "category": "Law"},
    {"id": 7, "instructor": "Eda", "title": "Web Development with Python", "category": "Development"},
    {"id": 8, "instructor": "Eda", "title": "Python", "category": "Development"}
]


# Home Page (Default Page)
@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


# Get courses
@app.get("/courses")
async def get_all_courses():
    return courses_db


# Get courses by title (using path)
@app.get("/courses/{course_title}")
async def get_courses_by_title(course_title: str):
    courses = []
    for course in courses_db:
        if course.get("title").lower() == course_title.lower():
            courses.append(course)
    return courses


# Get course by id (using path) [this function will never be called because of the path similarity]
@app.get("/courses/{course_id}")
async def get_course_by_id(course_id: int):
    for course in courses_db:
        if course.get("id") == course_id:
            return course


# Get course by category (using query)
@app.get("/courses/")
async def get_courses_by_category(course_category: str):
    courses = []
    for course in courses_db:
        if course.get("category").lower() == course_category.lower():
            courses.append(course)
    return courses


# Get courses by instructor and category (using path and query)
@app.get("/courses/{course_instructor}/")
async def get_courses_by_instructor_and_category(course_instructor: str, course_category: str):
    courses = []
    for course in courses_db:
        if course.get("instructor").lower() == course_instructor.lower() and \
           course.get("category").lower() == course_category.lower():
           courses.append(course)
    return courses


################################################################################################### END OF GET METHODS


# Add new row in table
@app.post("/courses/create_course")
async def create_course(course: Course):
    courses_db.append(course.model_dump())
    return {"message": "Course added successfully", "course": course}


################################################################################################### END OF POST METHODS


# Update a row in table
@app.put("/courses/update_course")
async def update_course(course: Course):
    course_dict = course.model_dump()
    for i in range(len(courses_db)):
        if courses_db[i].get("id") == course_dict.get("id"):
            courses_db[i] = course_dict
            return {"message": "Course updated successfully", "course": course_dict}

    raise HTTPException(status_code=404, detail="Course not found")


################################################################################################### END OF PUT METHODS


# Remove a row from table
@app.delete("/courses/delete_course/{course_id}")
async def delete_course(course_id: int):
    print(f"Received DELETE request for course_id: {course_id}")
    for index, course in enumerate(courses_db):
        if course["id"] == course_id:
            deleted_course = courses_db.pop(index)
            return {"message": "Course deleted successfully", "deleted_course": deleted_course}

    raise HTTPException(status_code=404, detail="Course not found")