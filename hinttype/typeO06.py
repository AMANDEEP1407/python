# 

email : str | None = None

email="aa@gmail.com"

print(email)


def fun(f:str|None = None):
    return f


print(fun("aman@gmail.com"))

def fun01(id: int|None = None) -> int|None:
    if id == 2:
        print(f"ID is Valid : {id}")
    else:
        print(f"Invalid Id : {id}")

fun01(2)
