def handle(func):
    def wrapper(*args,**kwargs):
        print("start")
        f=func(*args,**kwargs)
        print(f)
        print("end")
        return f
    return wrapper

@handle
def check(a,b):
    return a+b

check(3,4)