from pathlib import Path
import json

numbers=[1,23,4,5,6]

path=Path('numbers.json')
content=json.dumps(numbers)
path.write_text(content)


