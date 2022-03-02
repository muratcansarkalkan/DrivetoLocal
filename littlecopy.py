# Library for 7Zip and OS reach
# Main code.
import py7zr
import os
import pandas as pd
import shutil

# Conversion of completed but unreleased teams database to a dictionary.
def listofteams():
    df = pd.read_excel('Book1.xlsx')
    d = (df.set_index('Team').T.to_dict('records')[0])
    return d

# Used for packing a folder with a parent folder. mode r is for read. w is for write
def copycomplete(pathnew,d):
    for k,v in d.items():
        if os.path.isdir(f'{pathnew}/{d.get(k)}') == True:
            shutil.copy("complete.txt", f'{pathnew}/{v}/complete.txt')
            # It will also check if the file is already written.

# Main function.
if __name__ == "__main__":
    pathbase=input("Specify the folder that you installed the game")
    pathnew=pathbase+"\data\stadium\FIFA"
    teamlist = listofteams()
    # list = retrievelist(pathnew)
    export = copycomplete(pathnew,teamlist)