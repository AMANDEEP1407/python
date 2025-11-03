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

        
u1=User("james","Bond",23)
u1.greet_user()
u1.desc_user()
u1.increment_login_attempts()       
u1.increment_login_attempts()       
u1.reset_login_attempts()   
u1.increment_login_attempts()    
