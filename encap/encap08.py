class Flight:
    def __init__(self,seats_available):
        self.__seats_available = seats_available
    
    def book_seat(self):
        self.__seats_available -= 1

    def avl_seat(self):
        print(f"Avl. seat:{self.__seats_available}")

f=Flight(22)
f.avl_seat()
f.book_seat()
f.avl_seat()