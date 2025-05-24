from fastapi  import HTTPException
from application.schemas.User import RegisterAction, UserResponse, UsersResponse, MiniUserResponse, UsernameResponse
from application.models.User import User as UserTable
from application.database.Session import session_instance
from typing  import List

class User:
    """Class for User"""

    def register(self, registerInfo: RegisterAction):
        user=UserTable(name=registerInfo.name,
                    email=registerInfo.email,
                    role=registerInfo.role
        )
        session_instance.write(user)

        if user is not None:
            raise HTTPException(status_code=201, detail="User registered successfully")

        raise HTTPException(status_code=500, detail="Internal Server Error")

    def getUser(self, id) -> UserResponse:
        user=session_instance.read_one(UserTable,id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse(
            name=user.name,
            email=user.email,
            role=user.role,
            books_borrowed=user.books_borrowed,
            current_borrows=user.current_borrows
        )

    #

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

    

    

