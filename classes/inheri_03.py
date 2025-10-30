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

class Privileges:
    def __init__(self):
       self.privileges=["can add post", "can delete post", "can ban user",]
       
    def  show_privileges(self):
        print("Admin Privileges:")
        for f in self.privileges:
            print(f'\n -{f}')



class Admin(User):
    def __init__(self,fname,lname,pnumber,location):
        super().__init__(fname,lname,pnumber,location)
       
        self.Privileges=Privileges()
    





a=Admin('ram','lal',344444444,'delhi')
a.describe_user()
a.Privileges.show_privileges()




