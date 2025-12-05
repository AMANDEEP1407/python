from typing import Annotated

# field: Annotated[type, metadata]

# base:Annotated[int,"this is Int"]

# base = 12

# print(base)

def fun(base:Annotated[str,"this is string"]):

    return base

print(fun("road"))
