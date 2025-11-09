class User:
    def __init__(self,username,password):
        self.username = username
        self.__password=password

    def check_pass(self,p):
        if self.__password == p:
            print(f"can access granted")

        else:
            print("Wrong Password!")
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def reset_pass(self,r):
        self._User__password=r
        print("password Reset")

a=Admin("aman","pass123")
a.check_pass("pass123")
a.reset_pass("aman12")
a.check_pass("pass123")