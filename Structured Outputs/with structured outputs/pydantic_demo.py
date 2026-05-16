from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    name: str = 'nitish'
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    cgpa: float =Field(default=0.0, gt=0.0, lt=10.0, description="CGPA must be between 0.0 and 10.0")  
new_student = {"name": "Alice", "email": "alice@example.com", "cgpa": 8.5}
old_student = {}
student = Student(**new_student)
student1 = Student(**old_student)
print(student,type(student))
print(student1,type(student1))
 
student_dict = dict(student)
print(student_dict['age'])
student_json = student.model_dump_json()
print(student_json)
# coerce -> automatic type conversion -> Type coarsing
# Builtin-validation
# Field Function -> gt -> greater than, lt -> less than, ge -> greater than or equal to, le -> less than or equal to, description -> description for the field
