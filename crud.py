
from typing import List
from xml.dom import ValidationErr
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: str
    email: EmailStr

class UserService:
    def __init__(self):
        self.user: List[User] = []
    
    def create_user(self, data: dict):
        user = User(**data)
        self.user.append(user) #thêm vào List
        return user
    
    def get_all(self):
        result = [u.model_dump() for u in self.user]
        return result

service = UserService()

service.create_user({
    "id": 1,
    "name": "Alex",
    "email": "alex@gmail.com" 
})

service.create_user({
    "id": 2,
    "name": "Peter",
    "email": "peter@gmail.com" 
})

print(service.get_all())