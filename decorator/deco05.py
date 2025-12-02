def handle(func):
    def wrapper(*args,**kwargs): 
        try:
            return func(*args,**kwargs)
        except Exception:
            print("Error Occured")
    return wrapper
@handle # check= handle(check)
def check(a,b):
    return a/b
print(check(3,4))