# A decorator is a function that takes another function,
# adds extra functionality to it,
# and returns a new improved function.

# You use it when you want to wrap logic around a function without changing its code.



def my_deco(func):
    def wrapper():  #wrapper A new function that adds extra features around your function.
        print("start Wrapper")
        func()
        print("end wrapper")
    return wrapper

@my_deco
def check():
    print("this is check function")

check()

# def my_decorator(func):        # func = greet
#     def wrapper():
#         print("Before")
#         func()                 # this is greet()
#         print("After")
#     return wrapper

# @my_decorator   # greet = wrapper # actual things is  my_decorator(greet)
# def greet():
#     print("Hello Aman!")


# Step 1: You wrote greet()

# Step 2: Python sees @my_decorator

# Step 3: Python calls:
#         my_decorator(greet)

# Step 4: Inside the decorator,
#         func == greet

# Step 5: Decorator returns wrapper

# Step 6: greet = wrapper
