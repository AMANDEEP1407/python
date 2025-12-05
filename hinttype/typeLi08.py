from typing import Literal
# The value must be one of the specified fixed values
# ❌ No other value is allowed

# This is very useful for:

# roles

# status

# modes

# categories

# flags

# yes/no choices

base: Literal['Accept','Block']

base='Accept'
print(base)

# def fun(base:Literal["Admin","Role"]):
#     b=print(base)
#     return b

# fun("Admin")
def fun() -> Literal["Admin","Role"]:
    
    return 'Admin'

print(fun())