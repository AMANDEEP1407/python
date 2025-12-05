# def fun(t:tuple[int,str]) -> tuple[int,str]:
#     return t

# print(fun((3,"three")))
def fun01(t:tuple[tuple[int,...],tuple[str,int]]) -> tuple[tuple[int,...],tuple[str,int]]:
    return t

print(fun01(((2,3,4),('a',3))))