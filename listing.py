from pathlib import Path
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')
list = []

for path in Path().rglob(f'*.7z'):
    path = str(path)
    path = path + ("\n")
    list.append(path)

contents = open(f'Contents {date}.txt', 'w', encoding="utf-8")
    
contents.write("Here is the list of stadiums in this bundle:\n")

for element in list:
    contents.write(element)