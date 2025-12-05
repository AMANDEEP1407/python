from typing import Union

value : str | int = 20

# value="Twenty"

print(value)

def fun(x:int | float) -> int| float:
    return x*x 

print(fun(4))

