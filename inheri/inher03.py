class Restro:
    def __init__(self,name,dish,number_served=0):
        self.name=name
        self.dish=dish
        self.number_served=number_served

    def describe_restro(self):
        return f"name:{self.name} and Dishes:{self.dish}"
    
    def served(self):
        print(f"No of Serving:{self.number_served}")

    def set_number_served(self):
        print(f"the {self.number_served} customers that have been served")

    def inc_number_served(self,nowserved):
        self.number_served= self.number_served + nowserved
    
    def open_restro(self):
        print(f"{self.name} is Open")



# class IceCreamStand(Restro):
#     def __init__(self):
#         super().__init__(name,dish,number_served=0)

restro=Restro("PhalwanDaba","Indian",56)
restro.open_restro()
print(restro.describe_restro())
restro.served()
restro.set_number_served()
restro.inc_number_served(11)
restro.set_number_served()