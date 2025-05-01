

class User:

    def __init__(self, name=None, email=None, role=None,):
        self._name = name
        self._email = email
        self._role = role

    def register(self, name, email, role):
        self.__init__(name, email, role)

        db_user = UserTable(username=self._username, fullname=self._fullname, email=self._email, 
                            phone=self._phoneNumber, hashed_password=AuthHandler.get_password_hash(password))
        with Database.get_session() as session:
            session.add(db_user)
            session.commit()
            session.refresh(db_user)
            login_response = self.login(username, password)
            return LoginResponse(access_token=login_response.access_token, token_type=login_response.token_type)
