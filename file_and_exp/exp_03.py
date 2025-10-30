from pathlib import Path

try:
    path=Path('cat_file.txt')

    content=path.read_text()
    print(content)
except FileNotFoundError:
    print("file is not avalible")