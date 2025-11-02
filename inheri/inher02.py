class Restro:
    def __init__(self,name,dish):
        self.name=name
        self.dish=dish

    def describe_restro(self):
        return f"name:{self.name} and Dishes:{self.dish}"
    
    def open_restro(self):
        print(f"{self.name} is Open")

restro=Restro("PhalwanDaba","Indian")
restro.open_restro()
print(restro.describe_restro())