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
res=Restaurant('Taj','indian')
res.increment_number_served(23)
print(res.number_served)
res.increment_number_served(25)
print(res.number_served)
res.increment_number_served(29)
print(f"total Customer:{res.number_served}")