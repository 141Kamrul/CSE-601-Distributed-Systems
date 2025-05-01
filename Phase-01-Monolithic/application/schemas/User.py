from pydantic  import BaseModel

class  UserRegister:
    name: str
    email: str
    role: str