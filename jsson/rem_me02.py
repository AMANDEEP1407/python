from pathlib import Path
import json

path=Path('usernameA.json')



   
def greet_user():
    content=path.read_text()
    dic=json.loads(content)
    print(f'Welcome back! Name :{dic["name:"]}\nLocation:{dic['location:']}\n class:{dic['class:']}')

   
def  get_new_username():
    name=input("what's your Name:")
    location=input("what is your location:")
    classs=input("your Class:")
    dic={"name:":name,
         "location:":location,
         "class:":classs
         }
    content=json.dumps(dic)
    path.write_text(content)
    print(f'Next remember my Name :{dic['name:']}\nLocation:{dic['location:']}')

if path.exists():
    content=path.read_text()
    dic=json.loads(content)
    print(f'The current username is :{dic['name:']} --> yes/no')
    c= input("yes or no:")
    if c == 'yes':
        greet_user()
    elif c == 'no':
        get_new_username()

else:
    get_new_username()
