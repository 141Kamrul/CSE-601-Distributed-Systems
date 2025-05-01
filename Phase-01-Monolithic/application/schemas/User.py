from pydantic  import BaseModel

class RegisterAction(BaseModel):
    name: str
    email: str
    role: str

class RegisterResponse(BaseModel):
    message:  str

class UserResponse(BaseModel):
    user_id: int
    name: str
    email: str
    role: str