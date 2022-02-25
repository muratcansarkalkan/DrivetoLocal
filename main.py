# Library for 7Zip and OS reach
# Main code.
import py7zr
import os
import pandas as pd

# Conversion of team database to a dictionary. Not yet implemented
# def listofteams(list):
#     df = pd.read_excel(list)
#     df = df.iloc[ : , 1:]
#     d = (df.set_index('Team').T.to_dict('records')[0])

# Used for retrieving the available stadiums.
def retrievelist(pathnew):
    # We used scandir instead of listdir. os.listdir(path) gives str. os.scandir(path) gave list instead
    # If scanned paths are a directory then the name will be given.
    list = ([f.name for f in os.scandir(pathnew) if f.is_dir()])
    return list

# Fine, you'll specify only main path.

# Used for packing a folder with a parent folder. mode r is for read. w is for write
def pack(list,pathnew):
    for ID in list:
        # Now, if the complete.txt is included in the folder, then it will be packed.
        if os.path.isfile(f'{pathnew}/{ID}/complete.txt') == True:
            with py7zr.SevenZipFile(f'{ID}.7z', mode = "w") as archive:
                archive.writeall(f"{pathnew}/{ID}", f"data\stadium\FIFA\{ID}")

# Progress 25.2.2022: Now we are able to pack what we want and have what we want.
# Progress 25.2.2022: I can pack 7z's that has the empty file "complete.txt"

# # Used for extracting a folder.
# def unpack(ID):
#     with py7zr.SevenZipFile(f"{ID}.7z", mode="r") as archive:
#         archive.extractall()

# Main function.
if __name__ == "__main__":
    pathbase=input("Specify the folder that you installed the game")
    pathnew=pathbase+"\data\stadium\FIFA"
    list = retrievelist(pathnew)
    export = pack(list,pathnew)