from fastapi  import HTTPException
from application.schemas.User import RegisterResponse, RegisterAction, UserResponse
from application.models.User import User as UserTable
from application.database.Session import session_instance
from typing  import List

class User:

    def register(self, registerInfo: RegisterAction) -> RegisterResponse:
        try:
            user=UserTable(username=registerInfo.name,
                           email=registerInfo.email,
                           role=registerInfo.role
                        )
            session_instance.write(user)
            return RegisterResponse(message="User registered succesfully")
        except:
            return RegisterResponse(message="Registration failed")

    def getUsers(self) -> List[UserResponse]:
        users=session_instance.read_all(UserTable)
        print(users)
        userResponses=[]
        for user in  users:
            userResponses.append(
                UserResponse(
                    user_id=user.id,
                    name=user.username,
                    email=user.email,
                    role=user.role
                )
            )
        return userResponses

    def getUser(self, id) -> UserResponse:
        user=session_instance.read_one(UserTable,id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse(
            user_id=user.id,
            name=user.username,
            email=user.email,
            role=user.role
        )