class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
            print(f'restaurant_name:{self.restaurant_name} and cuisine_type:{self.cuisine_type}')
    def open_restaurant(self):
            print(f'the {self.restaurant_name} is open')
    def set_number_served(self,log):
          self.number_served=log

    def increment_number_served(self,km):
          self.number_served+=km    
class Icecreamstand(Restaurant):
      def __init__(self,restaurant_name,cuisine_type):
            super().__init__(restaurant_name,cuisine_type)
            self.flavors=['red','blue']

      def show_fl(self):
            for f in self.flavors:
                  print(f"Flavors:{f}")

    


r=Icecreamstand("taj","indian")
r.show_fl()