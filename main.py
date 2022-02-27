# Library for 7Zip and OS reach
# Main code.
import py7zr
import os
import pandas as pd

# Conversion of team database to a dictionary. Not yet implemented
def listofteams():
    df = pd.read_excel('TeamsMini.xlsx')
    d = (df.set_index('Team').T.to_dict('records')[0])
    return d

# Used for retrieving the available stadiums. This applies to end user. not me
# def retrievelist(pathnew):
#     # We used scandir instead of listdir. os.listdir(path) gives str. os.scandir(path) gave list of folders instead
#     # If scanned paths are a directory then the name will be given.
#     list = ([f.name for f in os.scandir(pathnew) if f.is_dir()])
#     return list

# Used for packing a folder with a parent folder. mode r is for read. w is for write
def pack(pathnew,d):
    for k, v in d.items():
    # Now, if the complete.txt is included in the folder, then it will be packed.
        if os.path.isfile(f'{pathnew}/{v}/complete.txt') == True:
            # It will also check if the file is already written.
            if os.path.exists(f'{k} - {v}.7z') == False:
                with py7zr.SevenZipFile(f'{k} - {v}.7z', mode = "w") as archive:
                    archive.writeall(f"{pathnew}/{v}", f"data\stadium\FIFA\{v}")

# Main function.
if __name__ == "__main__":
    pathbase=input("Specify the folder that you installed the game")
    pathnew=pathbase+"\data\stadium\FIFA"
    teamlist = listofteams()
    # list = retrievelist(pathnew)
    export = pack(pathnew,teamlist)