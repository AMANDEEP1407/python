from pathlib import Path
import json
path=Path('favnum.json')

 
  
def favnum():
 if path.exists():
    content=path.read_text()
    a=json.loads(content)
    print(f"{a} is the your number")
 else:
   create_fav(path)
   
   
   



def create_fav(path):
 fav=int(input("Enter your fav Number:"))
 content=json.dumps(fav)

 path.write_text(content)

favnum()