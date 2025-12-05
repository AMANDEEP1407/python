def fun(detail:dict[str,int]) -> dict[str,int]:
    return detail
print(fun({"name":22}))

# Dict of Dicts (Nested Dict)
def fun1(d:dict[str:dict[str,int]]):
    return d
print(fun1({"user1":{"score":2}}))
