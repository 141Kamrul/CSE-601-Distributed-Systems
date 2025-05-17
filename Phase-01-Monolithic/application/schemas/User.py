from pydantic  import BaseModel

class RegisterAction(BaseModel):
    name: str
    email: str
    role: str

class RegisterResponse(BaseModel):
    message:  str

class UserResponse(BaseModel):
    name: str
    email: str
    role: str

class UsersResponse(BaseModel):
    user_id: int
    name: str
    email: str
    role: str

class MiniUserResponse(BaseModel):
    user_id: int
    name: str
    email: str

class UsernameResponse(BaseModel):
    name: str
