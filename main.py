# Library for 7Zip and OS reach
# Main code.
import py7zr
import os

# Used for retrieving the available stadiums.
def retrievelist(path):
    # We used scandir instead of listdir. os.listdir(path) gives str. os.scandir(path) gave list instead
    # If scanned paths are a directory then the name will be given.
    list = ([f.name for f in os.scandir(path+"\data\stadium\FIFA") if f.is_dir()])
    return list

# Fine, you'll specify only main path.

# Used for packing a folder with a parent folder. mode r is for read. w is for write
def pack(list):
    for ID in list:
        # Example; if ID starts with 0001, then only they will be packed. Still WIP
        if ID.startswith("0001") == True:
            with py7zr.SevenZipFile(f'{ID}.7z', mode = "w") as archive:
                archive.writeall(f"{ID}", f"data\stadium\FIFA\{ID}")

# Progress 25.2.2022: Now we are able to pack what we want and have what we want.
# Next: I will pack 7z's that has the empty file "complete.txt"

# # Used for extracting a folder.
# def unpack(ID):
#     with py7zr.SevenZipFile(f"{ID}.7z", mode="r") as archive:
#         archive.extractall()

# Main function.
if __name__ == "__main__":
    path=input("Specify the folder that you installed the game")
    list = retrievelist(path)
    export = pack(list)