from fastapi import APIRouter
from application.crud.User import User
from application.schemas.User import RegisterAction, RegisterResponse, UserResponse
from typing import List

router=APIRouter(prefix='',tags=['User'])

user=User()

@router.post("/register/", response_model=RegisterResponse)
def register(registerInfo: RegisterAction):
    return user.register(registerInfo)

@router.get("/getusers/", response_model=List[UserResponse])
def getUsers():
    return user.getUsers()

@router.get("/getuser/{id}",  response_model=UserResponse)
def getUser(id):
    return user.getUser(id)