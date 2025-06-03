from fastapi import APIRouter
from application.crud.User import User
from application.schemas.User import RegisterAction, UserResponse

router=APIRouter(prefix='',tags=['User'])

user=User()

@router.post("/users/")
def register(registerInfo: RegisterAction):
    return user.register(registerInfo)

@router.get("/users/{id}",  response_model=UserResponse)
def getUser(id):
    return user.getUser(id)