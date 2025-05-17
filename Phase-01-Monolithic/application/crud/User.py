from fastapi  import HTTPException
from application.schemas.User import RegisterResponse, RegisterAction, UserResponse, UsersResponse, MiniUserResponse, UsernameResponse
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

    def getUsers(self) -> List[UsersResponse]:
        users=session_instance.read_all(UserTable)
        print(users)
        usersResponses=[]
        for user in  users:
            usersResponses.append(
                UsersResponse(
                    user_id=user.id,
                    name=user.username,
                    email=user.email,
                    role=user.role
                )
            )
        return usersResponses

    def getUser(self, id) -> UserResponse:
        user=session_instance.read_one(UserTable,id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse(
            name=user.username,
            email=user.email,
            role=user.role
        )

    def getMiniUser(self, id) -> MiniUserResponse:
        user=session_instance.read_one(UserTable,id)
        return MiniUserResponse(
            user_id=user.id,
            name=user.username,
            email=user.email
        )

    def getTotalUser(self):
        return session_instance.count_all(UserTable)

    def getUsername(self, id):
        user=session_instance.read_one(UserTable,id)
        return UsernameResponse(name=user.username)

    

    

