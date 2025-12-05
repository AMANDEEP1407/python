name : str = "john"
age: int = 22
Pect : float = 67.97
is_admin : bool = False

print(name)
print("Type: ",type(name))
print("Type: ",type(age))
print("Type: ",type(Pect))
print("Type: ",type(is_admin))
print("------------------------------")
def fun(fname:str):
    return f"Name :{fname}"

print(fun("Paul"))

