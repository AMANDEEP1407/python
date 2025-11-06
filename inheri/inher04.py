class User:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.login_attempts=0

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"total Logins :{self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts=0
        print(f"Reset Login to : {self.login_attempts}")
        

    def desc_user(self):
        print(f"Name:{self.fname} {self.lname} and age is {self.age}")

    def greet_user(self):
        print(f"Hello ! {self.fname} {self.lname}")
class Privileges:
    def __init__(self):
        self.privileges=[ "can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Admin have Privileges")
        for f in self.privileges:
            print(f"---privileges:{f}")

class Admin(User,Privileges):
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)

        
        

    



u1=User("james","Bond",23)
u2=Admin("john","Bond",23)
u2.desc_user()
u2.show_privileges()



# u1.greet_user()
# u1.desc_user()
# u1.increment_login_attempts()       
# u1.increment_login_attempts()       
# u1.reset_login_attempts()   
# u1.increment_login_attempts()    

