from pathlib import Path

path=Path('article.txt')
content=path.read_text()
print(content.lower().count('the'))
print(content)