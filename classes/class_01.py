class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
            print(f'restaurant_name:{self.restaurant_name} and cuisine_type:{self.cuisine_type}')
    def open_restaurant(self):
            print(f'the {self.restaurant_name} is open')

r1=Restaurant('pikazo','indian')
r2=Restaurant('hayat','indian')
r3=Restaurant('taj','indian')

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()