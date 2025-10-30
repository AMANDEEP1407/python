# def pizza(*args):
#     for a in args:

#         print(f"{a} is ordered sandwich")

# pizza('tomato','corn')

def profile(first,last,**kwargs):
    print('this is profile:')
    kwargs['first']=first
    kwargs['last']=last
    return kwargs

# p=profile('Amandeep','Singh',location='chandigarh',profile='python dev')
# print(p)

def car_info(company,model,**kwargs):
    print(f"Here's your cars {model}")
    kwargs['Company']=company
    kwargs['model']=model
    return kwargs

c=car_info('toyota','fortuner',color='black',gear='Manuall')
print(c)