# def fun1(*args):
#     list1=[x+x for x in args]
    


    
#     return f'{list1}' 

# a=fun1(1,2,3,4)
# print(a)

def fun2(**kwargs):
     for x,y in kwargs.items():
          return f"{x}:{y}"
    


    
     

b=fun2(name='deepali',classs=12)
print(b)