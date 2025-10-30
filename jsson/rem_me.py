from pathlib import Path
import json

path=Path('username.json')


if path.exists():
    content=path.read_text()
    a=json.loads(content)
    print(f"Welcome BAck ! {a}")

    
   
else:
    name=input("what's your Name:")
    content=json.dumps(name)
    path.write_text(content)
    print(f'Next remember my Name :{content}')