from pathlib import Path
import py7zr

gamepath = input("Specify game path")
for pathe in Path().rglob('*.7z'):
    with py7zr.SevenZipFile(pathe, mode="r") as archive:
        archive.extractall(path=gamepath)