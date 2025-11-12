

from dataclasses import dataclass
from pydantic import BaseModel, EmailStr, ValidationError


# class User:
#     def __init__(self, id, name, email):
#         self.id = id
#         self.name = name
#         self.email = email
# # create object 
# user = User(1, "An", "an@example.com")

# print(user.name)
# print(user.email)

# @dataclass
# class User:
#     id: int
#     full_name: str
#     email: str
#     active: bool = True

# user = User(1, "An", "an@gmail.com")
# print(user)

# pydantic

class User(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    active: bool = True
try:
    user = User(id=1, full_name="An", email="an@gmail.com", active=False)
    print(user.dict())
except ValidationError as e:
    print(e)
    