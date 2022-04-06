from pathlib import Path
import py7zr
import os

gamepath = input("Specify game path")

country = input("What country's stadiums do you want?\n")
print("For list of countries please check folders and type the folder names")

for pathe in Path().rglob(f'{country}\*.7z'):
    path1 = pathe
    pathe = str(pathe)
    pathe = pathe.replace('\\0', '//0')
    pathe = pathe.split('/')
    pathe = pathe[2]
    with py7zr.SevenZipFile(path1, mode="r") as archive:
        if os.path.exists(f'{gamepath}/data/stadium/FIFA/{pathe[0:8]}') == False:
        # Removed folder check function as the user will extract stadiums monthly.
            archive.extractall(path=gamepath)
        # else:
        #     continue