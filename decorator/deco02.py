i=0
def fun_called(func):
    def wrapper():
        print("stating ")
        func()
        print("ending ")
    return wrapper

@fun_called
def check():
    i=0
    i=i+1
    print(f"There is {i} times function called")
check()
check()
check()
check()
 