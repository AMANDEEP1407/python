class Pcar:
    def __init__(self,model,made):
        self.model=model
        self.made=made

    def detail(self):
        print(f"Name:{self.model} and Year:{self.made}")
    
class Ecar(Pcar):
    def __init__(self,model,made,battery):
        super().__init__(model,made)
        
        self.battery=Battery()
        
   
    
class Battery:
    def __init__(self,battery_size=40):
        self.battery_size=battery_size

    def des_battery(self):
        print(f"the battery size is {self.battery_size}")
        
# pcar1=Pcar("cemaro","2022")
# pcar1.detail()

ecar1=Ecar("Tesla","2022","40kwh")

ecar1.battery.des_battery()