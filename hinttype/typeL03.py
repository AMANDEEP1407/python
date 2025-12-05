numbers:list[int]=[2,3,4]
print(numbers)

print("---------------------------")
def fun01(Number:list[int]):
    return Number


print(fun01([1,2,3,5]))

print("---------------------------")

def fun02(number:list[int]) -> int:
    return sum(number)

print(fun02([1,2,34,5]))

print("List of lists---------------------------")
def fun3(Namelist:list[list[str]]):
    return Namelist

print(fun3([["aman","deep"],["john","Paul"]]))
class User:
    name:str
    age:int

u1=User()
u1.name="raman"
u1.age=22

u2=User()
u2.name="aman"
u2.age=22
users:list[User]=[u1,u2]
print(users)

