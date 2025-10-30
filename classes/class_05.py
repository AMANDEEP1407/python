class User:
    def __init__(self,fname,lname,pnumber,location):
        self.fname=fname
        self.lname=lname
        self.pnumber=pnumber
        self.location=location
        self.login_attempts=0

    def describe_user(self):
        print(f'name is {self.fname} {self.lname} and PhoneNumber is {self.pnumber} location:{self.location}')
        self.increment_login_attempts()
        print(f'login attemps:{self.login_attempts}')
    def greet_user(self):
        print(f"hello,{self.fname} {self.lname}")
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts=0
        print(f'login reset:{self.login_attempts}')
u1=User('raman','singh',432647434,'delhi')
u1.describe_user()
u1.reset_login_attempts()
u1.describe_user()
u1.describe_user()
u1.reset_login_attempts()
