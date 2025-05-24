from fastapi import APIRouter
from application.crud.User import User
from application.schemas.User import RegisterAction, UserResponse, UsersResponse
from typing import List

router=APIRouter(prefix='',tags=['User'])

user=User()

@router.post("/users/")
def register(registerInfo: RegisterAction):
    return user.register(registerInfo)

@router.get("/users/{id}",  response_model=UserResponse)
def getUser(id):
    return user.getUser(id)

#

@router.get("/getusers/", response_model=List[UsersResponse])
def getUsers():
    return user.getUsers()