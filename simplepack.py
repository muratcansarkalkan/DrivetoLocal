import py7zr
import os

# Used for packing a folder with a parent folder. mode r is for read. w is for write
def pack(ID):
    with py7zr.SevenZipFile(f'{ID}.7z', mode = "w") as archive:
        archive.writeall(f"{ID}", f"data\stadium\FIFA\{ID}")

# # Used for extracting a folder.
def unpack(ID):
    with py7zr.SevenZipFile(f"{ID}.7z", mode="r") as archive:
        archive.extractall()