def add_deco(func):
    def wrapper(*args,**kwargs):
       f=func(*args,**kwargs)
       print(f"function:{f}")
       return f
        
    return wrapper
@add_deco
def multi(a,b):
    c=a*b
    return c

multi(3,5)