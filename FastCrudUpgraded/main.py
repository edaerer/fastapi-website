from fastapi import FastAPI, Body, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Course:
    id: int
    title: str
    instructor: str
    rating: int
    published_date: int

    def __init__(self, id: int, title: str, instructor: str, rating: int, published_date: int):
        self.id = id
        self.title = title
        self.instructor = instructor
        self.rating = rating
        self.published_date = published_date


class CourseRequest(BaseModel):
    id: Optional[int] = Field(description="The course id is optional", default=None)
    title: str = Field(min_length=1, max_length=100)
    instructor: str = Field(min_length=2)
    rating: int = Field(gt=0, lt=11)
    published_date: int = Field(gt=2000)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "course title",
                "instructor": "course instructor",
                "rating": 10,
                "published_date": 2001,
            }
        }
    }

    def find_course_id(self):
        self.id = 1 if len(courses_db) == 0 else courses_db[-1].id + 1

courses_db = [
    Course(1, "Python", "Eda", 5, 2029),
    Course(2, "C#", "Elif", 3, 2030),
    Course(3, "C", "Talha", 6, 2031),
    Course(4, "Java", "Ece", 3, 2032),
    Course(5, "Cloud", "Nida", 7, 2032),
    Course(6, "AI/ML", "Eda", 10, 2032),
    Course(7, "DevOps", "Talha", 10, 2033),
]

@app.get("/courses", status_code=status.HTTP_200_OK)
async def get_courses():
    return courses_db


@app.get("/courses/{course_id}", status_code=status.HTTP_200_OK)
async def get_course(course_id: int = Path(gt=0)):
    for course in courses_db:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")


@app.get("/courses/", status_code=status.HTTP_200_OK)
async def get_courses_by_rating(course_rating: int = Query(gt=0, lt=11)):
    courses = []
    for course in courses_db:
        if course.rating == course_rating:
            courses.append(course)
    return courses


@app.get("/courses/publish/", status_code=status.HTTP_200_OK)
async def get_courses_by_published_date(course_published_date: int = Query()):
    courses = []
    for course in courses_db:
        if course.published_date == course_published_date:
            courses.append(course)
    return courses

####################################################################################################

@app.post("/create_course", status_code=status.HTTP_201_CREATED)
async def create_course(course_request: CourseRequest):
    course_request.find_course_id()
    new_course = Course(**course_request.model_dump())
    courses_db.append(new_course)


