class User:
    def __init__(self,fname,lname,pnumber,location):
        self.fname=fname
        self.lname=lname
        self.pnumber=pnumber
        self.location=location

    def describe_user(self):
        print(f'name is {self.fname} {self.lname} and PhoneNumber is {self.pnumber} location:{self.location}')

    def greet_user(self):
        print(f"hello,{self.fname} {self.lname}")

u1=User('john','doe',7740000000,'NYC')
u1=User('mil','doe',7740000001,'NYC')
u1=User('jemies','doe',7740000002,'NYC')

u1.greet_user()
u1.describe_user()